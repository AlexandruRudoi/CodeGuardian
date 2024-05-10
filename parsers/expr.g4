grammar Expr;

expression : additiveExpression ;

additiveExpression
    : multiplicativeExpression (('+' | '-') multiplicativeExpression)*
    ;

multiplicativeExpression
    : primaryExpression (('*' | '/') primaryExpression)*
    ;

primaryExpression
    : INTEGER
    | '(' expression ')'
    ;

INTEGER : [0-9]+ ;
WS : [ \t\r\n]+ -> skip ;
