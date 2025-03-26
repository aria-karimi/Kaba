# kaba/core/ast_nodes.py

class Node:
    """Base class for all AST nodes."""
    pass

# ───── Program ─────
class Program(Node):
    def __init__(self, statements):
        self.statements = statements  # list[Node]

# ───── Declarations ─────
class VariableDeclaration(Node):
    def __init__(self, typeName, suffix, varName, isArray=False, isClass=False):
        self.typeName = typeName  # e.g. "Düz", "Sulu", "Net", "Saçma", or class name
        self.suffix = suffix
        self.varName = varName
        self.isArray = isArray
        self.isClass = isClass

# ───── Assignment ─────
class Assignment(Node):
    def __init__(self, target, targetSuffix, value, valueSuffix):
        self.target = target  # Identifier, IndexAccess, or AttributeAccess
        self.targetSuffix = targetSuffix
        self.value = value    # Expression
        self.valueSuffix = valueSuffix

# ───── Statements ─────
class ExpressionStatement(Node):
    def __init__(self, expr):
        self.expr = expr

# ───── Control Flow ─────
class IfElse(Node):
    def __init__(self, condition, thenBlock, elseBlock=None):
        self.condition = condition # Expression
        self.thenBlock = thenBlock # Block
        self.elseBlock = elseBlock # Block or None


class WhileLoop(Node):
    def __init__(self, condition, body):
        self.condition = condition # Expression
        self.body = body           # Block


class ForLoop(Node):
    def __init__(self, loopVar, varSuffix, arrayExpr, arraySuffix, body):
        self.loopVar = loopVar
        self.varSuffix = varSuffix
        self.arrayExpr = arrayExpr
        self.arraySuffix = arraySuffix
        self.body = body

# ───── Exceptions ─────
class TryCatch(Node):
    def __init__(self, tryBlock, catchBlock):
        self.tryBlock = tryBlock
        self.catchBlock = catchBlock

class ThrowStatement(Node):
    def __init__(self, expr, suffix):
        self.expr = expr
        self.suffix = suffix

# ───── Blocks ─────
class Block(Node):
    def __init__(self, statements):
        self.statements = statements # list[Node]

class BlockWithReturn(Node):
    def __init__(self, statements, returnExpr):
        self.statements = statements # list[Node]
        self.returnExpr = returnExpr # Expression

# ───── Functions ─────
class FunctionDefinition(Node):
    def __init__(self, returnType, suffix, name, params, body):
        self.returnType = returnType
        self.suffix = suffix
        self.name = name
        self.params = params  # list[Parameter]
        self.body = body      # BlockWithReturn

class ReturnStatement(Node):
    def __init__(self, expr, suffix):
        self.expr = expr
        self.suffix = suffix

# ───── Function Parameters ─────
class Parameter(Node):
    def __init__(self, typeName, suffix, varName):
        self.typeName = typeName
        self.suffix = suffix
        self.varName = varName

# ───── Classes ─────
class ClassDefinition(Node):
    def __init__(self, name, attributes, methods):
        self.name = name
        self.attributes = attributes  # list[VariableDeclaration]
        self.methods = methods        # list[FunctionDefinition]

# ───── Expressions ─────
class Expression(Node):
    pass

class Literal(Expression):
    def __init__(self, value, valueType):
        self.value = value            # e.g., kırkiki, üçvirgülondört, Siker, Sikmez, "bokbir"
        self.valueType = valueType    # "Düz", "Sulu", "Net", "Saçma"

class Identifier(Expression):
    def __init__(self, name):
        self.name = name

class BinaryOp(Expression):
    def __init__(self, left, leftSuffix, op, right, rightSuffix):
        self.left = left
        self.leftSuffix = leftSuffix
        self.op = op  # e.g. "kat", "çak", "aynı"
        self.right = right
        self.rightSuffix = rightSuffix

class UnaryOp(Expression):
    def __init__(self, op, suffix, operand):
        self.op = op  # e.g. "tersi"
        self.suffix = suffix
        self.operand = operand

class FunctionCall(Expression):
    def __init__(self, name, args):
        self.name = name
        self.args = args  # list[Expression]

class IndexAccess(Expression):
    def __init__(self, arrayName, arraySuffix, indexExpr, indexSuffix):
        self.arrayName = arrayName
        self.arraySuffix = arraySuffix
        self.indexExpr = indexExpr
        self.indexSuffix = indexSuffix

class AttributeAccess(Expression):
    def __init__(self, objectName, objectSuffix, memberName, memberSuffix):
        self.objectName = objectName
        self.objectSuffix = objectSuffix
        self.memberName = memberName
        self.memberSuffix = memberSuffix