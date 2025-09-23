parser grammar CppParser;

options {
    tokenVocab = CppLexer;
}

// main
compilationUnit: translationUnit? EOF;

translationUnit: 
    (namespaceDefinition | classDefinition | usingDeclaration | preprocessorDirective | functionDefinition)*;

// namespace
namespaceDefinition:
    NAMESPACE IDENTIFIER? LBRACE translationUnit RBRACE;

// klasa
classDefinition:
    classKey IDENTIFIER (COLON accessSpecifier? classInheritanceList)? LBRACE classBody RBRACE SEMICOLON?;

classKey: CLASS | STRUCT;

classInheritanceList:
    classInheritance (COMMA classInheritance)*;

classInheritance:
    accessSpecifier? IDENTIFIER;

classBody:
    (accessSpecifier COLON | memberDeclaration)*;

accessSpecifier:
    PUBLIC | PRIVATE | PROTECTED;

// memberi
memberDeclaration:
    (staticDeclaration | virtualDeclaration | friendDeclaration | templateDeclaration | 
     memberFunction | memberVariable | constructor | destructor | inlineMethod | 
     methodWithBody) SEMICOLON?;

staticDeclaration:
    STATIC (memberFunction | memberVariable);

virtualDeclaration:
    VIRTUAL (memberFunction | memberVariable);

friendDeclaration:
    FRIEND (IDENTIFIER | memberFunction);

templateDeclaration:
    TEMPLATE LT templateParameterList GT (classDefinition | memberFunction | memberVariable);

templateParameterList:
    templateParameter (COMMA templateParameter)*;

templateParameter:
    (CLASS | TYPENAME) IDENTIFIER;

// Member funkcije
memberFunction:
    (CONST | VOLATILE | INLINE | EXPLICIT | EXTERN | MUTABLE | REGISTER | AUTO)* 
    returnType functionName LPAREN parameterList? RPAREN (CONST | VOLATILE | OVERRIDE)*;

returnType:
    (CONST | VOLATILE | STATIC)* typeSpecifier;

typeSpecifier:
    (CONST | VOLATILE)* (IDENTIFIER | QUALIFIED_NAME) (LT templateArgumentList GT)? (MULT | BITAND | BITOR)*;

templateArgumentList:
    templateArgument (COMMA templateArgument)*;

templateArgument:
    typeSpecifier | INTEGER_LITERAL | IDENTIFIER | QUALIFIED_NAME;

functionName:
    IDENTIFIER | operatorName;

operatorName:
    OPERATOR operatorSymbol;

operatorSymbol:
    ASSIGN | PLUS | MINUS | MULT | DIV | MOD | LT | GT | LE | GE | EQ | NE | AND | OR | NOT | 
    BITAND | BITOR | XOR | LSHIFT | RSHIFT | INC | DEC | TILDE | QUESTION | 
    LPAREN RPAREN | LBRACKET RBRACKET;

parameterList:
    parameter (COMMA parameter)*;

parameter:
    (CONST | VOLATILE)* typeSpecifier IDENTIFIER? (ASSIGN defaultValue)?;

defaultValue:
    INTEGER_LITERAL | FLOATING_LITERAL | CHARACTER_LITERAL | STRING_LITERAL | IDENTIFIER | QUALIFIED_NAME;

// Member varijable
memberVariable:
    (CONST | VOLATILE | STATIC | MUTABLE | REGISTER | AUTO)* typeSpecifier IDENTIFIER (ASSIGN defaultValue)?;

// konstruktori
constructor:
    IDENTIFIER LPAREN parameterList? RPAREN (COLON memberInitializerList)? (LBRACE constructorBody RBRACE)?;

destructor:
    TILDE IDENTIFIER LPAREN RPAREN (LBRACE destructorBody RBRACE)?;

memberInitializerList:
    memberInitializer (COMMA memberInitializer)*;

memberInitializer:
    IDENTIFIER LPAREN argumentList? RPAREN;

argumentList:
    argument (COMMA argument)*;

argument:
    INTEGER_LITERAL | FLOATING_LITERAL | CHARACTER_LITERAL | STRING_LITERAL | IDENTIFIER | QUALIFIED_NAME;

// metode
inlineMethod:
    (VIRTUAL | CONST | VOLATILE | INLINE | STATIC)* returnType functionName LPAREN parameterList? RPAREN 
    (CONST | VOLATILE | OVERRIDE)* LBRACE methodBody RBRACE;

methodWithBody:
    (VIRTUAL | CONST | VOLATILE | INLINE | STATIC)* returnType functionName LPAREN parameterList? RPAREN 
    (CONST | VOLATILE | OVERRIDE)* LBRACE methodBody RBRACE;


methodBody:
    (OTHER | IDENTIFIER | QUALIFIED_NAME | STRING_LITERAL | INTEGER_LITERAL | 
     LBRACE | RBRACE | LPAREN | RPAREN | SEMICOLON | COMMA | DOT | ARROW | 
     SCOPE | ASSIGN | PLUS | MINUS | MULT | DIV | LT | GT | LE | GE | EQ | NE | 
     AND | OR | NOT | BITAND | BITOR | XOR | LSHIFT | RSHIFT | INC | DEC | 
     TILDE | QUESTION | COLON | LBRACKET | RBRACKET)*;

constructorBody:
    (OTHER | IDENTIFIER | QUALIFIED_NAME | STRING_LITERAL | INTEGER_LITERAL | 
     LBRACE | RBRACE | LPAREN | RPAREN | SEMICOLON | COMMA | DOT | ARROW | 
     SCOPE | ASSIGN | PLUS | MINUS | MULT | DIV | LT | GT | LE | GE | EQ | NE | 
     AND | OR | NOT | BITAND | BITOR | XOR | LSHIFT | RSHIFT | INC | DEC | 
     TILDE | QUESTION | COLON | LBRACKET | RBRACKET)*;

destructorBody:
    (OTHER | IDENTIFIER | QUALIFIED_NAME | STRING_LITERAL | INTEGER_LITERAL | 
     LBRACE | RBRACE | LPAREN | RPAREN | SEMICOLON | COMMA | DOT | ARROW | 
     SCOPE | ASSIGN | PLUS | MINUS | MULT | DIV | LT | GT | LE | GE | EQ | NE | 
     AND | OR | NOT | BITAND | BITOR | XOR | LSHIFT | RSHIFT | INC | DEC | 
     TILDE | QUESTION | COLON | LBRACKET | RBRACKET)*;


functionDefinition:
    returnType IDENTIFIER LPAREN parameterList? RPAREN LBRACE functionBody RBRACE;

functionBody:
    (OTHER | IDENTIFIER | QUALIFIED_NAME | STRING_LITERAL | INTEGER_LITERAL | 
     LBRACE | RBRACE | LPAREN | RPAREN | SEMICOLON | COMMA | DOT | ARROW | 
     SCOPE | ASSIGN | PLUS | MINUS | MULT | DIV | LT | GT | LE | GE | EQ | NE | 
     AND | OR | NOT | BITAND | BITOR | XOR | LSHIFT | RSHIFT | INC | DEC | 
     TILDE | QUESTION | COLON | LBRACKET | RBRACKET)*;

// using deklaracija
usingDeclaration:
    USING (IDENTIFIER | NAMESPACE IDENTIFIER) SEMICOLON;

// direktive
preprocessorDirective:
    PREPROCESSOR;