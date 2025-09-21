lexer grammar CppLexer;

// Keywords
CLASS: 'class';
STRUCT: 'struct';
PUBLIC: 'public';
PRIVATE: 'private';
PROTECTED: 'protected';
VIRTUAL: 'virtual';
STATIC: 'static';
CONST: 'const';
VOLATILE: 'volatile';
INLINE: 'inline';
FRIEND: 'friend';
TEMPLATE: 'template';
NAMESPACE: 'namespace';
USING: 'using';
TYPEDEF: 'typedef';
ENUM: 'enum';
UNION: 'union';
OVERRIDE: 'override';
EXPLICIT: 'explicit';
EXTERN: 'extern';
MUTABLE: 'mutable';
REGISTER: 'register';
AUTO: 'auto';

// Access modifiers
COLON: ':';
SEMICOLON: ';';
COMMA: ',';
DOT: '.';
ARROW: '->';
SCOPE: '::';

// Brackets
LBRACE: '{';
RBRACE: '}';
LPAREN: '(';
RPAREN: ')';
LBRACKET: '[';
RBRACKET: ']';

// Operators
ASSIGN: '=';
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
MOD: '%';
LT: '<';
GT: '>';
LE: '<=';
GE: '>=';
EQ: '==';
NE: '!=';
AND: '&&';
OR: '||';
NOT: '!';
BITAND: '&';
BITOR: '|';
XOR: '^';
LSHIFT: '<<';
RSHIFT: '>>';

// Increment/Decrement
INC: '++';
DEC: '--';

// Special characters
TILDE: '~';
QUESTION: '?';

// Literals
INTEGER_LITERAL: [0-9]+;
FLOATING_LITERAL: [0-9]+ '.' [0-9]* | '.' [0-9]+;
CHARACTER_LITERAL: '\'' (~['\\\r\n] | '\\' .) '\'';
STRING_LITERAL: '"' (~["\\\r\n] | '\\' .)* '"';

// Identifiers
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;

// Qualified names (e.g., std::string)
QUALIFIED_NAME: IDENTIFIER (SCOPE IDENTIFIER)+;

// Whitespace and comments
WS: [ \t\r\n]+ -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;

// Preprocessor directives
PREPROCESSOR: '#' ~[\r\n]* -> skip;

// Everything else (for method bodies, etc.)
OTHER: .;