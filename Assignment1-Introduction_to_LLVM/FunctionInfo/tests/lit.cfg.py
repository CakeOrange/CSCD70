import lit
from lit.llvm import llvm_config


config.name = 'FunctionInfo'
config.test_format = lit.formats.ShTest(not llvm_config.use_lit_shell)
config.suffixes = ['.c', '.ll']

llvm_config.add_tool_substitutions(
        ["clang", "opt", "FileCheck"],
        config.llvm_config_bindir)
