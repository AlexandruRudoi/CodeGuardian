#include <iostream>
#include "ExprLexer.h"
#include "ExprParser.h"
#include "antlr4-runtime.h"

using namespace antlr4;

int main(int argc, const char* argv[]) {
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " <expression>" << std::endl;
        return 1;
    }

    ANTLRInputStream input(argv[1]);
    ExprLexer lexer(&input);
    CommonTokenStream tokens(&lexer);
    ExprParser parser(&tokens);

    tree::ParseTree* tree = parser.expression();
    std::cout << tree->toStringTree(&parser) << std::endl;

    return 0;
}
