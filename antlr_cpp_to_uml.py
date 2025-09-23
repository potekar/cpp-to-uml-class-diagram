#!/usr/bin/env python3
"""
Glavna skripta za konverziju C++ koda u UML dijagrame klasa koristeći ANTLR4.
"""

import sys
import os
import argparse
from antlr_visitor import parse_cpp_file_with_antlr
from antlr_plantuml_generator import AntlrPlantUMLGenerator
from semantic_analyzer import SemanticAnalyzer


def convert_cpp_to_uml(input_file: str, output_file: str = None, generate_diagram: bool = False, skip_semantic: bool = False) -> bool:
    """Konvertuje C++ fajl u UML dijagram klasa koristeći ANTLR4."""
    
    print(f"Konvertujem {input_file} u UML dijagram klasa (ANTLR4)...")
    
    # Parsiraj C++ fajl koristeći ANTLR4
    classes = parse_cpp_file_with_antlr(input_file)
    
    if not classes:
        print("Nisu pronađene klase u ulaznom fajlu.")
        return False
    
    print(f"Pronađeno {len(classes)} klasa:")
    for cls in classes:
        print(f"  - {cls.name} ({'struct' if cls.is_struct else 'class'})")
        print(f"    Članovi: {len(cls.members)}, Metode: {len(cls.methods)}")
    
    # Semantička analiza
    if not skip_semantic:
        print("\nIzvršavam semantičku analizu...")
        semantic_analyzer = SemanticAnalyzer()
        semantic_errors = semantic_analyzer.analyze_classes(classes)
        semantic_analyzer.print_analysis()
    else:
        print("\nPreskačem semantičku analizu...")
    
    # Generiši PlantUML kod
    generator = AntlrPlantUMLGenerator()
    for cls in classes:
        generator.add_class(cls)
    
    # Odredi izlazni fajl
    if output_file is None:
        base_name = os.path.splitext(os.path.basename(input_file))[0]
        output_file = f"output/{base_name}_class_diagram.puml"
    
    # Sačuvaj PlantUML kod
    generator.save_to_file(output_file)
    
    # Generiši dijagram ako je traženo
    if generate_diagram:
        print("Generišem UML dijagram...")
        success = generator.generate_diagram()
        if success:
            print("Dijagram uspešno generisan!")
        else:
            print("Neuspešno generisanje dijagrama. PlantUML kod je sačuvan u fajl.")
    
    return True


def main():
    
    
    # Proveri da li ulazni fajl postoji
    if not os.path.exists(args.input_file):
        print(f"Greška: Ulazni fajl '{args.input_file}' ne postoji.")
        sys.exit(1)
    
    # Konvertuj fajl
    success = convert_cpp_to_uml(
        args.input_file, 
        args.output, 
        args.generate_diagram,
        args.no_semantic
    )
    
    if success:
        print("Konverzija uspešno završena!")
    else:
        print("Konverzija neuspešna!")
        sys.exit(1)


if __name__ == "__main__":
    main()
