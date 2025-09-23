#!/usr/bin/env python3
"""
Semantička analiza  C++ koda.
"""

from typing import Dict, List, Set
from antlr_visitor import ClassInfo


class SemanticError:
    """Jednostavna semantička greška."""
    
    def __init__(self, message: str, error_type: str = "ERROR"):
        self.message = message
        self.error_type = error_type  # ERROR, WARNING
    
    def __str__(self):
        return f"{self.error_type}: {self.message}"


class SemanticAnalyzer:
    """Jednostavna semantička analiza."""
    
    def __init__(self):
        self.errors: List[SemanticError] = []
        self.warnings: List[SemanticError] = []
        self.classes: Dict[str, ClassInfo] = {}
        self.builtin_types = {"int", "float", "double", "char", "bool", "void", "string"}
    
    def analyze_classes(self, classes: List[ClassInfo]) -> List[SemanticError]:
        """Analizira klase i vraća greške."""
        self.errors.clear()
        self.warnings.clear()
        
        # Registruj sve klase
        for class_info in classes:
            self.classes[class_info.name] = class_info
        
        # Analiziraj svaku klasu
        for class_info in classes:
            self._analyze_class(class_info)
        
        return self.errors + self.warnings
    
    def _analyze_class(self, class_info: ClassInfo):
        """Analizira jednu klasu."""
        
        # 1. Proveri nasleđivanje
        self._check_inheritance(class_info)
        
        # 2. Proveri članove
        self._check_members(class_info)
        
        # 3. Proveri metode
        self._check_methods(class_info)
        
        # 4. Proveri konstruktore
        self._check_constructors(class_info)
    
    def _check_inheritance(self, class_info: ClassInfo):
        """Proverava nasleđivanje."""
        for base_class in class_info.base_classes:
            if base_class not in self.classes:
                self.errors.append(SemanticError(
                    f"Bazna klasa '{base_class}' nije definisana za klasu '{class_info.name}'"
                ))
            else:
                # Proveri cirkularno nasleđivanje
                if self._has_circular_inheritance(class_info.name, base_class):
                    self.errors.append(SemanticError(
                        f"Cirkularno nasleđivanje: {class_info.name} -> {base_class}"
                    ))
    
    def _has_circular_inheritance(self, class_name: str, base_class: str, visited: Set[str] = None) -> bool:
        """Proverava cirkularno nasleđivanje."""
        if visited is None:
            visited = set()
        
        if class_name in visited:
            return True
        
        if base_class not in self.classes:
            return False
        
        visited.add(class_name)
        
        for parent in self.classes[base_class].base_classes:
            if self._has_circular_inheritance(base_class, parent, visited.copy()):
                return True
        
        return False
    
    def _check_members(self, class_info: ClassInfo):
        """Proverava članove klase."""
        member_names = set()
        
        for member in class_info.members:
            # Proveri duplikate
            if member.name in member_names:
                self.errors.append(SemanticError(
                    f"Duplikat člana '{member.name}' u klasi '{class_info.name}'"
                ))
            member_names.add(member.name)
            
            # Proveri tip
            if not self._is_valid_type(member.member_type):
                self.warnings.append(SemanticError(
                    f"Nepoznat tip '{member.member_type}' za član '{member.name}' u klasi '{class_info.name}'",
                    "WARNING"
                ))
    
    def _check_methods(self, class_info: ClassInfo):
        """Proverava metode klase."""
        method_names = set()
        
        for method in class_info.methods:
            # Proveri duplikate
            if method.name in method_names:
                self.errors.append(SemanticError(
                    f"Duplikat metode '{method.name}' u klasi '{class_info.name}'"
                ))
            method_names.add(method.name)
            
            # Proveri tip povratne vrednosti
            if not self._is_valid_type(method.member_type):
                self.warnings.append(SemanticError(
                    f"Nepoznat tip povratne vrednosti '{method.member_type}' za metodu '{method.name}'",
                    "WARNING"
                ))
            
            # Proveri parametre
            for param_type, param_name in method.parameters:
                if not self._is_valid_type(param_type):
                    self.warnings.append(SemanticError(
                        f"Nepoznat tip parametra '{param_type}' za metodu '{method.name}'",
                        "WARNING"
                    ))
    
    def _check_constructors(self, class_info: ClassInfo):
        """Proverava konstruktore."""
        constructor_names = set()
        
        for constructor in class_info.constructors:
            # Proveri duplikate
            if constructor.name in constructor_names:
                self.errors.append(SemanticError(
                    f"Duplikat konstruktora '{constructor.name}' u klasi '{class_info.name}'"
                ))
            constructor_names.add(constructor.name)
            
            # Proveri parametre
            for param_type, param_name in constructor.parameters:
                if not self._is_valid_type(param_type):
                    self.warnings.append(SemanticError(
                        f"Nepoznat tip parametra '{param_type}' za konstruktor '{constructor.name}'",
                        "WARNING"
                    ))
    
    def _is_valid_type(self, type_str: str) -> bool:
        """Proverava da li je tip validan."""
        if not type_str or type_str == "unknown":
            return False
        
        type_str = type_str.strip()
        
        # Ukloni pointer i reference oznake
        base_type = type_str.replace('*', '').replace('&', '').replace('const', '').strip()
        
        # Proveri da li je builtin tip
        if base_type in self.builtin_types:
            return True
        
        # Proveri da li je klasa
        if base_type in self.classes:
            return True
        
        # Proveri template tipove (osnovno)
        if '<' in base_type:
            template_base = base_type.split('<')[0].strip()
            return template_base in self.builtin_types or template_base in self.classes
        
        return False
    
    def get_analysis_summary(self) -> Dict[str, any]:
        """Vraća sažetak analize."""
        return {
            "total_errors": len(self.errors),
            "total_warnings": len(self.warnings),
            "classes_analyzed": len(self.classes),
            "errors": [str(error) for error in self.errors],
            "warnings": [str(warning) for warning in self.warnings]
        }
    
    def print_analysis(self):
        """Ispisuje rezultate analize."""
        print("\n=== SEMANTIČKA ANALIZA ===")
        print(f"Analizirano klasa: {len(self.classes)}")
        print(f"Greške: {len(self.errors)}")
        print(f"Upozorenja: {len(self.warnings)}")
        
        if self.errors:
            print("\n--- GREŠKE ---")
            for error in self.errors:
                print(f"  {error}")
        
        if self.warnings:
            print("\n--- UPOZORENJA ---")
            for warning in self.warnings:
                print(f"  {warning}")
        
        print("=" * 30)
