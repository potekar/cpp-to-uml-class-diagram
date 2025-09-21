#!/usr/bin/env python3
"""
ANTLR4 Visitor za C++ klase.
"""

from antlr4 import *
from grammar.CppLexer import CppLexer
from grammar.CppParser import CppParser
from grammar.CppParserListener import CppParserListener


class ClassInfo:
    """Informacije o C++ klasi."""
    
    def __init__(self, name, is_struct=False):
        self.name = name
        self.is_struct = is_struct
        self.base_classes = []
        self.members = []
        self.methods = []
        self.constructors = []
        self.destructors = []
        self.current_access = "private"
        
    def add_member(self, member):
        """Dodaje član varijablu."""
        member.access_level = self.current_access
        self.members.append(member)
        
    def add_method(self, method):
        """Dodaje metodu."""
        method.access_level = self.current_access
        self.methods.append(method)
        
    def add_constructor(self, constructor):
        """Dodaje konstruktor."""
        constructor.access_level = self.current_access
        self.constructors.append(constructor)
        
    def add_destructor(self, destructor):
        """Dodaje destruktor."""
        destructor.access_level = self.current_access
        self.destructors.append(destructor)


class MemberInfo:
    """Informacije o članu klase."""
    
    def __init__(self, name, member_type="", is_static=False, is_virtual=False, is_const=False):
        self.name = name
        self.member_type = member_type
        self.is_static = is_static
        self.is_virtual = is_virtual
        self.is_const = is_const
        self.access_level = "private"
        self.parameters = []
        
    def add_parameter(self, param_type, param_name=""):
        """Dodaje parametar metodi."""
        self.parameters.append((param_type, param_name))


class CppASTVisitor(CppParserListener):
    """ANTLR4 Visitor za C++ AST."""
    
    def __init__(self):
        self.classes = []
        self.current_class = None
        self.current_access = "private"
        
    def enterClassDefinition(self, ctx):
        """Ulazak u definiciju klase."""
        class_name = ctx.IDENTIFIER().getText()
        is_struct = ctx.classKey().STRUCT() is not None
        
        self.current_class = ClassInfo(class_name, is_struct)
        
        # Parsiraj nasleđivanje
        if ctx.classInheritanceList():
            for inheritance in ctx.classInheritanceList().classInheritance():
                base_class = inheritance.IDENTIFIER().getText()
                self.current_class.base_classes.append(base_class)
    
    def exitClassDefinition(self, ctx):
        """Izlazak iz definicije klase."""
        if self.current_class:
            self.classes.append(self.current_class)
            self.current_class = None
    
    def enterAccessSpecifier(self, ctx):
        """Ulazak u access specifier."""
        if ctx.PUBLIC():
            self.current_access = "public"
        elif ctx.PRIVATE():
            self.current_access = "private"
        elif ctx.PROTECTED():
            self.current_access = "protected"
    
    def enterMemberVariable(self, ctx):
        """Ulazak u član varijablu."""
        if not self.current_class:
            return
            
        # Izdvoji ime varijable
        var_name = ctx.IDENTIFIER().getText()
        
        # Izdvoji tip
        var_type = self._extract_type_from_context(ctx)
        
        # Proveri modifikatore
        is_static = any(child.getText() == 'static' for child in ctx.children)
        is_const = any(child.getText() == 'const' for child in ctx.children)
        
        member = MemberInfo(var_name, var_type, is_static, False, is_const)
        member.access_level = self.current_access
        self.current_class.add_member(member)
    
    def enterMemberFunction(self, ctx):
        """Ulazak u metodu."""
        if not self.current_class:
            return
            
        # Izdvoji ime metode
        func_name = ctx.functionName().getText()
        
        # Izdvoji tip povratne vrednosti
        return_type = self._extract_return_type_from_context(ctx)
        
        # Proveri modifikatore
        is_static = any(child.getText() == 'static' for child in ctx.children)
        is_virtual = any(child.getText() == 'virtual' for child in ctx.children)
        is_const = any(child.getText() == 'const' for child in ctx.children)
        
        method = MemberInfo(func_name, return_type, is_static, is_virtual, is_const)
        method.access_level = self.current_access
        
        # Izdvoji parametre
        if ctx.parameterList():
            for param in ctx.parameterList().parameter():
                param_type = self._extract_parameter_type(param)
                param_name = param.IDENTIFIER().getText() if param.IDENTIFIER() else ""
                method.add_parameter(param_type, param_name)
        
        self.current_class.add_method(method)
    
    def enterInlineMethod(self, ctx):
        """Ulazak u inline metodu."""
        if not self.current_class:
            return
            
        # Izdvoji ime metode
        func_name = ctx.functionName().getText()
        
        # Izdvoji tip povratne vrednosti
        return_type = self._extract_return_type_from_context(ctx)
        
        # Proveri modifikatore
        is_static = any(child.getText() == 'static' for child in ctx.children)
        is_virtual = any(child.getText() == 'virtual' for child in ctx.children)
        is_const = any(child.getText() == 'const' for child in ctx.children)
        
        method = MemberInfo(func_name, return_type, is_static, is_virtual, is_const)
        method.access_level = self.current_access
        
        # Izdvoji parametre
        if ctx.parameterList():
            for param in ctx.parameterList().parameter():
                param_type = self._extract_parameter_type(param)
                param_name = param.IDENTIFIER().getText() if param.IDENTIFIER() else ""
                method.add_parameter(param_type, param_name)
        
        self.current_class.add_method(method)
    
    def enterMethodWithBody(self, ctx):
        """Ulazak u metodu sa telom."""
        if not self.current_class:
            return
            
        # Izdvoji ime metode
        func_name = ctx.functionName().getText()
        
        # Izdvoji tip povratne vrednosti
        return_type = self._extract_return_type_from_context(ctx)
        
        # Proveri modifikatore
        is_static = any(child.getText() == 'static' for child in ctx.children)
        is_virtual = any(child.getText() == 'virtual' for child in ctx.children)
        is_const = any(child.getText() == 'const' for child in ctx.children)
        
        method = MemberInfo(func_name, return_type, is_static, is_virtual, is_const)
        method.access_level = self.current_access
        
        # Izdvoji parametre
        if ctx.parameterList():
            for param in ctx.parameterList().parameter():
                param_type = self._extract_parameter_type(param)
                param_name = param.IDENTIFIER().getText() if param.IDENTIFIER() else ""
                method.add_parameter(param_type, param_name)
        
        self.current_class.add_method(method)
    
    def enterConstructor(self, ctx):
        """Ulazak u konstruktor."""
        if not self.current_class:
            return
            
        constructor_name = ctx.IDENTIFIER().getText()
        constructor = MemberInfo(constructor_name, "", False, False, False)
        constructor.access_level = self.current_access
        
        # Izdvoji parametre
        if ctx.parameterList():
            for param in ctx.parameterList().parameter():
                param_type = self._extract_parameter_type(param)
                param_name = param.IDENTIFIER().getText() if param.IDENTIFIER() else ""
                constructor.add_parameter(param_type, param_name)
        
        self.current_class.add_constructor(constructor)
    
    def enterDestructor(self, ctx):
        """Ulazak u destruktor."""
        if not self.current_class:
            return
            
        destructor_name = "~" + ctx.IDENTIFIER().getText()
        destructor = MemberInfo(destructor_name, "", False, False, False)
        destructor.access_level = self.current_access
        
        self.current_class.add_destructor(destructor)
    
    def _extract_type_from_context(self, ctx):
        """Izdvaja tip iz konteksta."""
        type_parts = []
        for child in ctx.children:
            if hasattr(child, 'getText'):
                text = child.getText()
                if text not in ['static', 'const', 'volatile', 'inline', '=']:
                    type_parts.append(text)
        
        return ' '.join(type_parts[:-1]) if len(type_parts) > 1 else "unknown"
    
    def _extract_return_type_from_context(self, ctx):
        """Izdvaja tip povratne vrednosti iz konteksta."""
        type_parts = []
        for child in ctx.children:
            if hasattr(child, 'getText'):
                text = child.getText()
                if text not in ['static', 'virtual', 'const', 'volatile', 'inline', 'override']:
                    type_parts.append(text)
        
        # Ukloni ime metode iz tipa
        if type_parts and type_parts[-1] in ['info', 'getName', 'getAge', 'getStudentId']:
            type_parts = type_parts[:-1]
        
        return ' '.join(type_parts) if type_parts else "void"
    
    def _extract_parameter_type(self, param_ctx):
        """Izdvaja tip parametra iz konteksta."""
        type_parts = []
        for child in param_ctx.children:
            if hasattr(child, 'getText'):
                text = child.getText()
                if text not in ['const', 'volatile', '=']:
                    type_parts.append(text)
        
        return ' '.join(type_parts[:-1]) if len(type_parts) > 1 else "unknown"


def parse_cpp_file_with_antlr(filename):
    """Parsira C++ fajl koristeći ANTLR4."""
    try:
        # Učitaj fajl
        with open(filename, 'r', encoding='utf-8') as f:
            input_stream = f.read()
        
        # Kreiraj lexer i parser
        lexer = CppLexer(InputStream(input_stream))
        token_stream = CommonTokenStream(lexer)
        parser = CppParser(token_stream)
        
        # Parsiraj
        tree = parser.compilationUnit()
        
        # Kreiraj visitor
        visitor = CppASTVisitor()
        walker = ParseTreeWalker()
        walker.walk(visitor, tree)
        
        return visitor.classes
        
    except FileNotFoundError:
        print(f"Greška: Fajl '{filename}' nije pronađen.")
        return []
    except Exception as e:
        print(f"Greška pri parsiranju: {e}")
        return []
