parser grammar CppParser;

options {
    tokenVocab = CppLexer;
}

// Main entry point
compilationUnit: translationUnit? EOF;

translationUnit: 
    (namespaceDefinition | classDefinition | usingDeclaration | preprocessorDirective | functionDefinition)*;

// Namespace definitions
namespaceDefinition:
    NAMESPACE IDENTIFIER? LBRACE translationUnit RBRACE;

// Class definitions
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

// Member declarations
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

// Member functions
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

// Member variables
memberVariable:
    (CONST | VOLATILE | STATIC | MUTABLE | REGISTER | AUTO)* typeSpecifier IDENTIFIER (ASSIGN defaultValue)?;

// Constructors and destructors
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

// Inline methods with bodies
inlineMethod:
    (VIRTUAL | CONST | VOLATILE | INLINE | STATIC)* returnType functionName LPAREN parameterList? RPAREN 
    (CONST | VOLATILE | OVERRIDE)* LBRACE methodBody RBRACE;

methodWithBody:
    (VIRTUAL | CONST | VOLATILE | INLINE | STATIC)* returnType functionName LPAREN parameterList? RPAREN 
    (CONST | VOLATILE | OVERRIDE)* LBRACE methodBody RBRACE;

// Method bodies (allow any content)
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

// Function definitions (for main, etc.)
functionDefinition:
    returnType IDENTIFIER LPAREN parameterList? RPAREN LBRACE functionBody RBRACE;

functionBody:
    (OTHER | IDENTIFIER | QUALIFIED_NAME | STRING_LITERAL | INTEGER_LITERAL | 
     LBRACE | RBRACE | LPAREN | RPAREN | SEMICOLON | COMMA | DOT | ARROW | 
     SCOPE | ASSIGN | PLUS | MINUS | MULT | DIV | LT | GT | LE | GE | EQ | NE | 
     AND | OR | NOT | BITAND | BITOR | XOR | LSHIFT | RSHIFT | INC | DEC | 
     TILDE | QUESTION | COLON | LBRACKET | RBRACKET)*;

// Using declarations
usingDeclaration:
    USING (IDENTIFIER | NAMESPACE IDENTIFIER) SEMICOLON;

// Preprocessor directives
preprocessorDirective:
    PREPROCESSOR;