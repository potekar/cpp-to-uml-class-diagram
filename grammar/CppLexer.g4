lexer grammar CppLexer;

// kljucne rijeci
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

// operatori pristupa
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

// operatori
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

// inkrementacija/dekrementacija
INC: '++';
DEC: '--';

// specijalni karakteri
TILDE: '~';
QUESTION: '?';

// Literali
INTEGER_LITERAL: [0-9]+;
FLOATING_LITERAL: [0-9]+ '.' [0-9]* | '.' [0-9]+;
CHARACTER_LITERAL: '\'' (~['\\\r\n] | '\\' .) '\'';
STRING_LITERAL: '"' (~["\\\r\n] | '\\' .)* '"';

// Identifikatori
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;

// kvalifikatori
QUALIFIED_NAME: IDENTIFIER (SCOPE IDENTIFIER)+;

// bjeline i komentari
WS: [ \t\r\n]+ -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;

// direktive
PREPROCESSOR: '#' ~[\r\n]* -> skip;

// ostalo
OTHER: .;