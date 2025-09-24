#!/usr/bin/env python3
"""
PlantUML generator za ANTLR4 klase.
"""

from antlr_visitor import ClassInfo

global filenameClass
class AntlrPlantUMLGenerator:
    
    
    def __init__(self):
        self.classes = []
    
    def add_class(self, class_info: ClassInfo):
        """Dodaje klasu u generator."""
        self.classes.append(class_info)
    
    def generate_plantuml_code(self) -> str:
        lines = ["@startuml"]
        lines.append("!theme plain")
        lines.append("")

        for class_info in self.classes:
            lines.extend(self._generate_class_definition(class_info))
            lines.append("")

        # Nasleđivanje
        for class_info in self.classes:
            for base_class in class_info.base_classes:
                lines.append(f"{base_class} <|-- {class_info.name}")

        lines.extend(self._generate_associations())

        lines.append("@enduml")
        return "\n".join(lines)

    def _generate_associations(self) -> list:
        """Dodaje linije za agregaciju (o--) i kompoziciju (*--)."""
        lines = []
        class_names = {c.name for c in self.classes}

        for class_info in self.classes:
            for member in class_info.members:
                if not member.member_type:
                    continue

                raw_type = member.member_type.strip()
            
                clean_type = raw_type.replace("const ", "").strip()
                base_type = clean_type.rstrip("*&")

                if base_type in class_names:
                    if "*" in clean_type or "&" in clean_type:
                    
                        lines.append(f"{class_info.name} o-- {base_type}")
                    else:
                        
                        lines.append(f"{class_info.name} *-- {base_type}")
        return lines
    def _generate_class_definition(self, class_info: ClassInfo) -> list:
        """Generiše PlantUML kod za jednu klasu."""
        lines = []
        
        # Zaglavlje klase
        class_type = "class"
        lines.append(f"{class_type} {class_info.name} {{")
        
        # Dodaj članove grupirane po nivou pristupa
        self._add_members_by_access(lines, class_info, "private", "-")
        self._add_members_by_access(lines, class_info, "protected", "#")
        self._add_members_by_access(lines, class_info, "public", "+")
        
        lines.append("}")
        return lines
    
    def _add_members_by_access(self, lines: list, class_info: ClassInfo, 
                              access_level: str, symbol: str):
        """Dodaje članove sa određenim nivoom pristupa u PlantUML kod."""
        
        # Dodaj član varijable
        for member in class_info.members:
            if member.access_level == access_level:
                member_line = f"  {symbol} {member.name}"
                if member.member_type:
                    member_line += f" : {member.member_type}"
                if member.is_static:
                    member_line += " {static}"
                if member.is_const:
                    member_line += " {readOnly}"
                lines.append(member_line)
        
        # Dodaj konstruktore
        for constructor in class_info.constructors:
            if constructor.access_level == access_level:
                constructor_line = f"  {symbol} {constructor.name}("
                if constructor.parameters:
                    param_list = []
                    for param_type, param_name in constructor.parameters:
                        if param_name:
                            param_list.append(f"{param_type} {param_name}")
                        else:
                            param_list.append(param_type)
                    constructor_line += ", ".join(param_list)
                constructor_line += ")"
                lines.append(constructor_line)
        
        # Dodaj destruktore
        for destructor in class_info.destructors:
            if destructor.access_level == access_level:
                lines.append(f"  {symbol} {destructor.name}()")
        
        # Dodaj metode
        for method in class_info.methods:
            if method.access_level == access_level:
                method_line = f"  {symbol} {method.name}("
                if method.parameters:
                    param_list = []
                    for param_type, param_name in method.parameters:
                        if param_name:
                            param_list.append(f"{param_type} {param_name}")
                        else:
                            param_list.append(param_type)
                    method_line += ", ".join(param_list)
                method_line += ")"
                
                if method.member_type and method.member_type != "void":
                    method_line += f" : {method.member_type}"
                
                if method.is_static:
                    method_line += " {static}"
                if method.is_virtual:
                    method_line += " {abstract}"
                if method.is_const:
                    method_line += " {readOnly}"
                
                lines.append(method_line)
    
    def save_to_file(self, filename: str):
        """Čuva PlantUML kod u fajl."""
        plantuml_code = self.generate_plantuml_code()
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(plantuml_code)
        print(f"PlantUML kod sačuvan u {filename}")
    
    def generate_diagram(self, output_format: str = "png") -> bool:
        """Generiše UML dijagram koristeći PlantUML."""
        import subprocess
        import os
        
        # Sačuvaj PlantUML kod u privremeni fajl
        
        temp_file = "temp_file"
        self.save_to_file(temp_file)
        plantuml_jar="plantuml.jar"
        
        try:
            
            # Generiši dijagram
            cmd = ["java", "-jar", plantuml_jar, f"-t{output_format}", "-o", "uml_diagrams", temp_file]
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"Dijagram uspešno generisan kao {output_format}")
                return True
            else:
                print(f"Greška pri generisanju dijagrama")
                return False
                
        except FileNotFoundError:
            print("Java nije pronađena. Molimo instalirajte Java za generisanje dijagrama.")
            return False
        finally:
            # Očisti privremeni fajl
            if os.path.exists(temp_file):
                os.remove(temp_file)
