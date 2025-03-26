# Generated from Kaba.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .KabaParser import KabaParser
else:
    from KabaParser import KabaParser

# This class defines a complete listener for a parse tree produced by KabaParser.
class KabaListener(ParseTreeListener):

    # Enter a parse tree produced by KabaParser#program.
    def enterProgram(self, ctx:KabaParser.ProgramContext):
        pass

    # Exit a parse tree produced by KabaParser#program.
    def exitProgram(self, ctx:KabaParser.ProgramContext):
        pass


    # Enter a parse tree produced by KabaParser#statement.
    def enterStatement(self, ctx:KabaParser.StatementContext):
        pass

    # Exit a parse tree produced by KabaParser#statement.
    def exitStatement(self, ctx:KabaParser.StatementContext):
        pass


    # Enter a parse tree produced by KabaParser#terminator.
    def enterTerminator(self, ctx:KabaParser.TerminatorContext):
        pass

    # Exit a parse tree produced by KabaParser#terminator.
    def exitTerminator(self, ctx:KabaParser.TerminatorContext):
        pass


    # Enter a parse tree produced by KabaParser#declarationStmt.
    def enterDeclarationStmt(self, ctx:KabaParser.DeclarationStmtContext):
        pass

    # Exit a parse tree produced by KabaParser#declarationStmt.
    def exitDeclarationStmt(self, ctx:KabaParser.DeclarationStmtContext):
        pass


    # Enter a parse tree produced by KabaParser#assignmentStmt.
    def enterAssignmentStmt(self, ctx:KabaParser.AssignmentStmtContext):
        pass

    # Exit a parse tree produced by KabaParser#assignmentStmt.
    def exitAssignmentStmt(self, ctx:KabaParser.AssignmentStmtContext):
        pass


    # Enter a parse tree produced by KabaParser#expressionStmt.
    def enterExpressionStmt(self, ctx:KabaParser.ExpressionStmtContext):
        pass

    # Exit a parse tree produced by KabaParser#expressionStmt.
    def exitExpressionStmt(self, ctx:KabaParser.ExpressionStmtContext):
        pass


    # Enter a parse tree produced by KabaParser#ifStmt.
    def enterIfStmt(self, ctx:KabaParser.IfStmtContext):
        pass

    # Exit a parse tree produced by KabaParser#ifStmt.
    def exitIfStmt(self, ctx:KabaParser.IfStmtContext):
        pass


    # Enter a parse tree produced by KabaParser#whileStmt.
    def enterWhileStmt(self, ctx:KabaParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by KabaParser#whileStmt.
    def exitWhileStmt(self, ctx:KabaParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by KabaParser#forStmt.
    def enterForStmt(self, ctx:KabaParser.ForStmtContext):
        pass

    # Exit a parse tree produced by KabaParser#forStmt.
    def exitForStmt(self, ctx:KabaParser.ForStmtContext):
        pass


    # Enter a parse tree produced by KabaParser#tryCatchStmt.
    def enterTryCatchStmt(self, ctx:KabaParser.TryCatchStmtContext):
        pass

    # Exit a parse tree produced by KabaParser#tryCatchStmt.
    def exitTryCatchStmt(self, ctx:KabaParser.TryCatchStmtContext):
        pass


    # Enter a parse tree produced by KabaParser#throwStmt.
    def enterThrowStmt(self, ctx:KabaParser.ThrowStmtContext):
        pass

    # Exit a parse tree produced by KabaParser#throwStmt.
    def exitThrowStmt(self, ctx:KabaParser.ThrowStmtContext):
        pass


    # Enter a parse tree produced by KabaParser#block.
    def enterBlock(self, ctx:KabaParser.BlockContext):
        pass

    # Exit a parse tree produced by KabaParser#block.
    def exitBlock(self, ctx:KabaParser.BlockContext):
        pass


    # Enter a parse tree produced by KabaParser#functionDef.
    def enterFunctionDef(self, ctx:KabaParser.FunctionDefContext):
        pass

    # Exit a parse tree produced by KabaParser#functionDef.
    def exitFunctionDef(self, ctx:KabaParser.FunctionDefContext):
        pass


    # Enter a parse tree produced by KabaParser#blockWithReturn.
    def enterBlockWithReturn(self, ctx:KabaParser.BlockWithReturnContext):
        pass

    # Exit a parse tree produced by KabaParser#blockWithReturn.
    def exitBlockWithReturn(self, ctx:KabaParser.BlockWithReturnContext):
        pass


    # Enter a parse tree produced by KabaParser#returnStmt.
    def enterReturnStmt(self, ctx:KabaParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by KabaParser#returnStmt.
    def exitReturnStmt(self, ctx:KabaParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by KabaParser#classDef.
    def enterClassDef(self, ctx:KabaParser.ClassDefContext):
        pass

    # Exit a parse tree produced by KabaParser#classDef.
    def exitClassDef(self, ctx:KabaParser.ClassDefContext):
        pass


    # Enter a parse tree produced by KabaParser#classMember.
    def enterClassMember(self, ctx:KabaParser.ClassMemberContext):
        pass

    # Exit a parse tree produced by KabaParser#classMember.
    def exitClassMember(self, ctx:KabaParser.ClassMemberContext):
        pass


    # Enter a parse tree produced by KabaParser#paramList.
    def enterParamList(self, ctx:KabaParser.ParamListContext):
        pass

    # Exit a parse tree produced by KabaParser#paramList.
    def exitParamList(self, ctx:KabaParser.ParamListContext):
        pass


    # Enter a parse tree produced by KabaParser#param.
    def enterParam(self, ctx:KabaParser.ParamContext):
        pass

    # Exit a parse tree produced by KabaParser#param.
    def exitParam(self, ctx:KabaParser.ParamContext):
        pass


    # Enter a parse tree produced by KabaParser#expression.
    def enterExpression(self, ctx:KabaParser.ExpressionContext):
        pass

    # Exit a parse tree produced by KabaParser#expression.
    def exitExpression(self, ctx:KabaParser.ExpressionContext):
        pass


    # Enter a parse tree produced by KabaParser#expr_or.
    def enterExpr_or(self, ctx:KabaParser.Expr_orContext):
        pass

    # Exit a parse tree produced by KabaParser#expr_or.
    def exitExpr_or(self, ctx:KabaParser.Expr_orContext):
        pass


    # Enter a parse tree produced by KabaParser#expr_and.
    def enterExpr_and(self, ctx:KabaParser.Expr_andContext):
        pass

    # Exit a parse tree produced by KabaParser#expr_and.
    def exitExpr_and(self, ctx:KabaParser.Expr_andContext):
        pass


    # Enter a parse tree produced by KabaParser#expr_cmp.
    def enterExpr_cmp(self, ctx:KabaParser.Expr_cmpContext):
        pass

    # Exit a parse tree produced by KabaParser#expr_cmp.
    def exitExpr_cmp(self, ctx:KabaParser.Expr_cmpContext):
        pass


    # Enter a parse tree produced by KabaParser#expr_add.
    def enterExpr_add(self, ctx:KabaParser.Expr_addContext):
        pass

    # Exit a parse tree produced by KabaParser#expr_add.
    def exitExpr_add(self, ctx:KabaParser.Expr_addContext):
        pass


    # Enter a parse tree produced by KabaParser#expr_mul.
    def enterExpr_mul(self, ctx:KabaParser.Expr_mulContext):
        pass

    # Exit a parse tree produced by KabaParser#expr_mul.
    def exitExpr_mul(self, ctx:KabaParser.Expr_mulContext):
        pass


    # Enter a parse tree produced by KabaParser#expr_unary.
    def enterExpr_unary(self, ctx:KabaParser.Expr_unaryContext):
        pass

    # Exit a parse tree produced by KabaParser#expr_unary.
    def exitExpr_unary(self, ctx:KabaParser.Expr_unaryContext):
        pass


    # Enter a parse tree produced by KabaParser#atom.
    def enterAtom(self, ctx:KabaParser.AtomContext):
        pass

    # Exit a parse tree produced by KabaParser#atom.
    def exitAtom(self, ctx:KabaParser.AtomContext):
        pass


    # Enter a parse tree produced by KabaParser#expressionList.
    def enterExpressionList(self, ctx:KabaParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by KabaParser#expressionList.
    def exitExpressionList(self, ctx:KabaParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by KabaParser#functionCall.
    def enterFunctionCall(self, ctx:KabaParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by KabaParser#functionCall.
    def exitFunctionCall(self, ctx:KabaParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by KabaParser#variableRef.
    def enterVariableRef(self, ctx:KabaParser.VariableRefContext):
        pass

    # Exit a parse tree produced by KabaParser#variableRef.
    def exitVariableRef(self, ctx:KabaParser.VariableRefContext):
        pass


    # Enter a parse tree produced by KabaParser#booleanLiteral.
    def enterBooleanLiteral(self, ctx:KabaParser.BooleanLiteralContext):
        pass

    # Exit a parse tree produced by KabaParser#booleanLiteral.
    def exitBooleanLiteral(self, ctx:KabaParser.BooleanLiteralContext):
        pass


    # Enter a parse tree produced by KabaParser#typeSpec.
    def enterTypeSpec(self, ctx:KabaParser.TypeSpecContext):
        pass

    # Exit a parse tree produced by KabaParser#typeSpec.
    def exitTypeSpec(self, ctx:KabaParser.TypeSpecContext):
        pass


    # Enter a parse tree produced by KabaParser#arrayRef.
    def enterArrayRef(self, ctx:KabaParser.ArrayRefContext):
        pass

    # Exit a parse tree produced by KabaParser#arrayRef.
    def exitArrayRef(self, ctx:KabaParser.ArrayRefContext):
        pass


    # Enter a parse tree produced by KabaParser#className.
    def enterClassName(self, ctx:KabaParser.ClassNameContext):
        pass

    # Exit a parse tree produced by KabaParser#className.
    def exitClassName(self, ctx:KabaParser.ClassNameContext):
        pass


    # Enter a parse tree produced by KabaParser#functionName.
    def enterFunctionName(self, ctx:KabaParser.FunctionNameContext):
        pass

    # Exit a parse tree produced by KabaParser#functionName.
    def exitFunctionName(self, ctx:KabaParser.FunctionNameContext):
        pass


    # Enter a parse tree produced by KabaParser#variableName.
    def enterVariableName(self, ctx:KabaParser.VariableNameContext):
        pass

    # Exit a parse tree produced by KabaParser#variableName.
    def exitVariableName(self, ctx:KabaParser.VariableNameContext):
        pass



del KabaParser