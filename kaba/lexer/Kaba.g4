grammar Kaba;

///////////////////////////////////////////////////////////////////////////////
// PARSER RULES
///////////////////////////////////////////////////////////////////////////////

program
    : (statement | functionDef | classDef)* EOF
    ;

statement
    : declarationStmt terminator
    | assignmentStmt terminator
    | expressionStmt terminator
    | ifStmt
    | whileStmt
    | forStmt
    | tryCatchStmt
    | throwStmt terminator
    ;

terminator
    : AMK
    | AMQ
    | AQ
    | AMIK
    | AMINAKOYUM
    ;

//////////////////////////////
// Declarations & Assignments
//////////////////////////////

declarationStmt
    // e.g. Düz Bok'tan bokbir çök
    : typeSpec BOK SUFFIX variableName ÇÖK
    | typeSpec BOK TORBASI SUFFIX variableName ÇÖK
    ;

assignmentStmt
    // e.g. bokbir'e bokiki'yi sok
    : variableRef SUFFIX expression SUFFIX SOK
    ;

expressionStmt
    : expression
    ;

//////////////////////////////
// Control Flow
//////////////////////////////

ifStmt
    : expression SIKTIYSE block (SIKMEDIYSE block)?
    ;

whileStmt
    : expression SIKERKEN block
    ;

forStmt
    // e.g. bok'u boktorbası'nda sallayarak hadi ... siktir
    : variableName SUFFIX arrayRef SUFFIX SALLAYARAK block
    ;

//////////////////////////////
// Exception Handling
//////////////////////////////

tryCatchStmt
    : DENESENE block SIÇARSA block
    ;

throwStmt
    // e.g. rezalet'i patlat amk
    : expression SUFFIX PATLAT
    ;

//////////////////////////////
// Blocks
//////////////////////////////

block
    : HADI statement* SIKTIR
    ;

//////////////////////////////
// Function Definitions
//////////////////////////////

functionDef
    // e.g. Düz Bok'tan hesapla şöyle Düz Bok x böyle hadi ... siktir
    : typeSpec BOK SUFFIX functionName paramList blockWithReturn
    ;

blockWithReturn
    : HADI statement* returnStmt SIKTIR
    ;

returnStmt
    // e.g. bokbir'i tükür amk
    : expression SUFFIX TÜKÜR terminator
    ;

//////////////////////////////
// Class Definitions
//////////////////////////////

classDef
    // e.g. Öğrenci Bok hadi ... siktir
    : className BOK HADI classMember* SIKTIR
    ;

classMember
    : declarationStmt terminator
    | functionDef
    ;

//////////////////////////////
// Parameters
//////////////////////////////

paramList
    // e.g. şöyle Düz Bok'tan bokbir virgül Sulu Bok'tan bokiki böyle
    : ŞÖYLE param (VIRGUL param)* BÖYLE
    | ŞÖYLE BÖYLE // possibly empty
    ;

param
    : typeSpec BOK SUFFIX variableName
    | typeSpec BOK TORBASI SUFFIX variableName
    ;

//////////////////////////////
// Expressions & Operator Precedence
//////////////////////////////

expression
    : expr_or
    ;

expr_or
    : expr_and (YA expr_and)*
    ;

expr_and
    : expr_cmp (VE expr_cmp)*
    ;

expr_cmp
    : expr_add (expr_add SUFFIX (KOYMUŞ | KOYMAMIŞ))*
    | expr_add (SUFFIX expr_add AYNI)*
    ;

expr_add
    : expr_mul (SUFFIX expr_mul SUFFIX (KAT | SÖK))*
    ;

expr_mul
    : expr_unary (SUFFIX expr_unary SUFFIX (ÇAK | YAR))*
    ;

expr_unary
    // e.g. (atom 'in) tersi or just atom
    : atom SUFFIX TERSI
    | atom
    ;

atom
    // parentheses
    : ŞÖYLE expressionList BÖYLE
    // function call
    | functionCall
    // variable reference
    | variableRef
    // boolean literal
    | booleanLiteral
    // entire string block
    | STRING_BLOCK
    // numeric literal will be proceccessed as identifiers
    ;

expressionList
    : expression (VIRGUL expression)*
    ;

functionCall
    : functionName ŞÖYLE expressionList BÖYLE
    | functionName ŞÖYLE BÖYLE
    ;

variableRef
    : variableName
    ;

booleanLiteral
    : SIKER    // true
    | SIKMEZ   // false
    ;

//////////////////////////////
// Types & References
//////////////////////////////

typeSpec
    // e.g. Düz, Sulu, Net, Saçma
    : (DÜZ | SULU | NET | SAÇMA)
    ;

arrayRef
    : variableRef
    ;

className
    : ID
    ;

functionName
    : ID
    ;

variableName
    : ID
    ;

///////////////////////////////////////////////////////////////////////////////
// LEXER RULES
///////////////////////////////////////////////////////////////////////////////

//---------------------------
// Main Keywords
//---------------------------
BOK           : 'Bok';
TORBASI       : 'Torbası';
BOKU          : 'boku';
KAT           : 'kat';
SÖK           : 'sök';
ÇAK           : 'çak';
YAR           : 'yar';
AYNI          : 'aynı';
TERSI         : 'tersi';
KOYMUŞ        : 'koymuş';
KOYMAMIŞ      : 'koymamış';
VE            : 've';
YA            : 'ya';
SIKTIYSE      : 'siktiyse';
SIKMEDIYSE    : 'sikmediyse';
SIKERKEN      : 'sikerken';
SALLAYARAK    : 'sallayarak';
ÇÖK           : 'çök';
TÜKÜR         : 'tükür';
DENESENE      : 'denesene';
SIÇARSA       : 'sıçarsa';
REZALET       : 'rezalet';
PATLAT        : 'patlat';
SOK           : 'sok';
ŞÖYLE         : 'şöyle';
BÖYLE         : 'böyle';
HADI          : 'hadi';
SIKTIR        : 'siktir';
DEMIŞ         : 'demiş';
DEMEMIŞ       : 'dememiş';
VIRGUL        : 'virgül';
AMK           : 'amk';
AMQ           : 'amq';
AQ            : 'aq';
AMIK          : 'amık';
AMINAKOYUM    : 'amınakoyum';

//---------------------------
// Data Types
//---------------------------
DÜZ           : 'Düz';
SULU          : 'Sulu';
NET           : 'Net';
SAÇMA         : 'Saçma';

//---------------------------
// Boolean Literals for Net
//---------------------------
SIKER         : 'Siker';   // true
SIKMEZ        : 'Sikmez';  // false

//---------------------------
// String Block: Everything between 'demiş' and 'dememiş'
//---------------------------
STRING_BLOCK
 : DEMIŞ .*? DEMEMIŞ
  ;

//---------------------------
// Single Generic Suffix
// e.g. 'tan', 'nin', 'i', etc.
//---------------------------
SUFFIX
 : '\'' TURKISH_LETTER+
  ;

//---------------------------
// Identifiers (Turkish letters only)
//---------------------------
ID
 : TURKISH_LETTER+
  ;

//---------------------------
// Fragment: Turkish Letter
//---------------------------
fragment TURKISH_LETTER
 : [abcçdefgğhıijklmnoöpqrsştuüvwxyzABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZ]
  ;

//---------------------------
// Whitespace & Unrecognized
//---------------------------
WS
 : [ \t\r\n]+ -> skip
 ;

UNRECOGNIZED
 : . -> skip
 ;