import sys
from antlr4 import FileStream, CommonTokenStream

from kaba.lexer.KabaLexer import KabaLexer
from kaba.lexer.KabaParser import KabaParser
from kaba.lexer.KabaVisitor import KabaVisitor

# --- Placeholder AST + Semantic + Transpiler stubs ---
# from kaba.core.ast_nodes import Program
# from kaba.semantic.semantic_checker import SemanticAnalyzer
# from kaba.transpiler.kaba_to_c import KabaToCTranspiler

class ASTBuilder(KabaVisitor):
    def visitProgram(self, ctx):
        print("[AST] Visiting program node (placeholder)")
        return "<AST placeholder>"

def main():
    if len(sys.argv) != 2:
        print("Usage: kaba <file.kaba>")
        sys.exit(1)

    input_file = sys.argv[1]
    if not input_file.endswith(".kaba"):
        print("Error: Input file must have a .kaba extension")
        sys.exit(1)

    try:
        # --- Phase 1: Lex + Parse ---
        input_stream = FileStream(input_file, encoding='utf-8')
        lexer = KabaLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = KabaParser(token_stream)
        tree = parser.program()

        # --- Phase 2: Build AST ---
        builder = ASTBuilder()
        ast = builder.visit(tree)
        print(f"[AST] Built AST: {ast}")

        # --- Phase 3: Semantic Analysis ---
        # analyzer = SemanticAnalyzer()
        # analyzer.analyze(ast)

        # --- Phase 4: Transpile to C ---
        # transpiler = KabaToCTranspiler()
        # c_code = transpiler.transpile(ast)
        # output_file = input_file.replace(".kaba", ".c")
        # with open(output_file, "w", encoding="utf-8") as f:
        #     f.write(c_code)
        # print(f"[Done] Transpiled to {output_file}")

    except Exception as e:
        print(f"[Error] {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()