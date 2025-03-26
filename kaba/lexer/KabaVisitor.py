# Generated from Kaba.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .KabaParser import KabaParser
else:
    from KabaParser import KabaParser

# This class defines a complete generic visitor for a parse tree produced by KabaParser.

class KabaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by KabaParser#program.
    def visitProgram(self, ctx:KabaParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KabaParser#statement.
    def visitStatement(self, ctx:KabaParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KabaParser#terminator.
    def visitTerminator(self, ctx:KabaParser.TerminatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KabaParser#declarationStmt.
    def visitDeclarationStmt(self, ctx:KabaParser.DeclarationStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KabaParser#assignmentStmt.
    def visitAssignmentStmt(self, ctx:KabaParser.AssignmentStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KabaParser#expressionStmt.
    def visitExpressionStmt(self, ctx:KabaParser.ExpressionStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KabaParser#ifStmt.
    def visitIfStmt(self, ctx:KabaParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KabaParser#whileStmt.
    def visitWhileStmt(self, ctx:KabaParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KabaParser#forStmt.
    def visitForStmt(self, ctx:KabaParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KabaParser#tryCatchStmt.
    def visitTryCatchStmt(self, ctx:KabaParser.TryCatchStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KabaParser#throwStmt.
    def visitThrowStmt(self, ctx:KabaParser.ThrowStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KabaParser#block.
    def visitBlock(self, ctx:KabaParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KabaParser#functionDef.
    def visitFunctionDef(self, ctx:KabaParser.FunctionDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KabaParser#blockWithReturn.
    def visitBlockWithReturn(self, ctx:KabaParser.BlockWithReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KabaParser#returnStmt.
    def visitReturnStmt(self, ctx:KabaParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KabaParser#classDef.
    def visitClassDef(self, ctx:KabaParser.ClassDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KabaParser#classMember.
    def visitClassMember(self, ctx:KabaParser.ClassMemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KabaParser#paramList.
    def visitParamList(self, ctx:KabaParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KabaParser#param.
    def visitParam(self, ctx:KabaParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KabaParser#expression.
    def visitExpression(self, ctx:KabaParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KabaParser#expr_or.
    def visitExpr_or(self, ctx:KabaParser.Expr_orContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KabaParser#expr_and.
    def visitExpr_and(self, ctx:KabaParser.Expr_andContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KabaParser#expr_cmp.
    def visitExpr_cmp(self, ctx:KabaParser.Expr_cmpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KabaParser#expr_add.
    def visitExpr_add(self, ctx:KabaParser.Expr_addContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KabaParser#expr_mul.
    def visitExpr_mul(self, ctx:KabaParser.Expr_mulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KabaParser#expr_unary.
    def visitExpr_unary(self, ctx:KabaParser.Expr_unaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KabaParser#atom.
    def visitAtom(self, ctx:KabaParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KabaParser#expressionList.
    def visitExpressionList(self, ctx:KabaParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KabaParser#functionCall.
    def visitFunctionCall(self, ctx:KabaParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KabaParser#variableRef.
    def visitVariableRef(self, ctx:KabaParser.VariableRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KabaParser#booleanLiteral.
    def visitBooleanLiteral(self, ctx:KabaParser.BooleanLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KabaParser#typeSpec.
    def visitTypeSpec(self, ctx:KabaParser.TypeSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KabaParser#arrayRef.
    def visitArrayRef(self, ctx:KabaParser.ArrayRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KabaParser#className.
    def visitClassName(self, ctx:KabaParser.ClassNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KabaParser#functionName.
    def visitFunctionName(self, ctx:KabaParser.FunctionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KabaParser#variableName.
    def visitVariableName(self, ctx:KabaParser.VariableNameContext):
        return self.visitChildren(ctx)



del KabaParser