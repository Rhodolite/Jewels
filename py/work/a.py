#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
import  Capital.Builtin                                                 #   Capital.Boot
import  Capital.Privileged                                              #   Capital.Boot
import  Capital.Shared                                                  #   Capital.Boot
import  PythonBuiltIn                                                   #   Capital.Boot
import  PythonException                                                 #   Capital.Boot
import  PythonSystem                                                    #   Capital.Boot

from    Capital.BuiltIn     import  __build_class                       #   Capital.Boot (Python 3 only)
from    Capital.BuiltIn     import  __import__                          #   Capital.Boot
from    Capital.BuiltIn     import  is_instance                         #   Capital.Boot
from    Capital.BuiltIn     import  privileged_2                        #   Capital.Core


    transport('Capital.Absent',                     'absent')
    transport('Capital.Ascii',                      'lookup_ascii')
    transport('Capital.Ascii',                      'unknown_ascii')
    transport('Capital.Cache2',                     'create_cache')
    transport('Capital.Cache2',                     'produce_conjure_by_name__V2')
    transport('Capital.Cache2',                     'produce_conjure_unique_dual')
    transport('Capital.Cache2',                     'produce_conjure_unique_dual__21')
    transport('Capital.Cache2',                     'produce_conjure_unique_triple')
    transport('Capital.Cache2',                     'produce_conjure_unique_triple__312')
    transport('Capital.Cache',                      'produce_cache_functions')
    transport('Capital.Cache',                      'produce_conjure_by_name')
    transport('Capital.Cache',                      'produce_conjure_dual')
    transport('Capital.Cache',                      'produce_conjure_dual__21')
    transport('Capital.Cache',                      'produce_conjure_single')
    transport('Capital.Cache',                      'produce_conjure_triple')
    transport('Capital.Cache',                      'produce_conjure_triple__312')
    transport('Capital.Cache',                      'produce_conjure_tuple')
    transport('Capital.Cadence',                    'cadence_constructing')
    transport('Capital.Cadence',                    'cadence_entered')
    transport('Capital.Cadence',                    'cadence_exception')
    transport('Capital.Cadence',                    'cadence_exited')
    transport('Capital.Cadence',                    'cadence_initialized')
    transport('Capital.Cadence',                    'cadence_reuse')
    transport('Capital.Codec',                      'encode_ascii')
    transport('Capital.ContextManager',             'empty_context_manager')
    transport('Capital.Core',                       'address_of')
    transport('Capital.Core',                       'arrange')
    transport('Capital.Core',                       'attribute')
    transport('Capital.Core',                       'Boolean')
    transport('Capital.Core',                       'Bytes')
    transport('Capital.Core',                       'character')
    transport('Capital.Core',                       'enumerate')
    transport('Capital.Core',                       'execute')
    transport('Capital.Core',                       'false')
    transport('Capital.Core',                       'FrozenSet')
    transport('Capital.Core',                       'globals')
    transport('Capital.Core',                       'Integer')
    transport('Capital.Core',                       'intern_arrange')
    transport('Capital.Core',                       'intern_integer')
    transport('Capital.Core',                       'intern_string')
    transport('Capital.Core',                       'introspection')
    transport('Capital.Core',                       'is_python_2')
    transport('Capital.Core',                       'is_python_3')
    transport('Capital.Core',                       'iterate')
    transport('Capital.Core',                       'iterate_range')
    transport('Capital.Core',                       'length')
    transport('Capital.Core',                       'line')
    transport('Capital.Core',                       'LiquidSet')
    transport('Capital.Core',                       'List')
    transport('Capital.Core',                       'Long')
    transport('Capital.Core',                       'Map')
    transport('Capital.Core',                       'maximum')
    transport('Capital.Core',                       'Method')
    transport('Capital.Core',                       'method_is_function')
    transport('Capital.Core',                       'minimum')
    transport('Capital.Core',                       'next_method')
    transport('Capital.Core',                       'none')
    transport('Capital.Core',                       'Object')
    transport('Capital.Core',                       'ordinal')
    transport('Capital.Core',                       'partial')
    transport('Capital.Core',                       'portray')
    transport('Capital.Core',                       'privileged')
    transport('Capital.Core',                       'property')
    transport('Capital.Core',                       'python_debug_mode')
    transport('Capital.Core',                       'raising_exception')
    transport('Capital.Core',                       'raising_exception_from')
    transport('Capital.Core',                       'rename')
    transport('Capital.Core',                       'rename_function')
    transport('Capital.Core',                       'Slice')
    transport('Capital.Core',                       'sorted_list')
    transport('Capital.Core',                       'static_method')
    transport('Capital.Core',                       'String')
    transport('Capital.Core',                       'sum')
    transport('Capital.Core',                       'true')
    transport('Capital.Core',                       'Tuple')
    transport('Capital.Core',                       'type')
    transport('Capital.Core',                       'Type')
    transport('Capital.DelayedFileOutput',          'create_DelayedFileOutput')
    transport('Capital.DumpCache',                  'dump_cache_to_string')
    transport('Capital.DumpCache',                  'print_cache')
    transport('Capital.Exception',                  'except_any_clause')
    transport('Capital.Exception',                  'except_clause')
    transport('Capital.Exception',                  'Exception')
    transport('Capital.Exception',                  'exit_clause')
    transport('Capital.Exception',                  'FileNotFoundError')
    transport('Capital.Exception',                  'finally_clause')
    transport('Capital.Exception',                  'ImportError')
    transport('Capital.Exception',                  'OSError')
    transport('Capital.Exception',                  'PermissionError')
    transport('Capital.Exception',                  'raise_runtime_error')
    transport('Capital.Exception',                  'raise_value_error')
    transport('Capital.Exception',                  'StopIteration')
    transport('Capital.Exception',                  'SystemExit')
    transport('Capital.GeneratedConjureQuadruple',  'produce_conjure_quadruple__4123')
    transport('Capital.Global',                     'capital_global')
    transport('Capital.Herd_2',                     'create_herd_2')
    transport('Capital.Herd',                       'empty_herd')
    transport('Capital.Horde',                      'create_horde_2')
    transport('Capital.Import',                     'import_module')
    transport('Capital.Map',                        'first_map_item')
    transport('Capital.Map',                        'iterate_items_sorted_by_key')
    transport('Capital.Map',                        'iterate_values_sorted_by_key')
    transport('Capital.Map',                        'values_tuple_sorted_by_key')
    transport('Capital.Map',                        'view_items')
    transport('Capital.Map',                        'view_values')
    transport('Capital.Method',                     'return_self')
    transport('Capital.Output',                     'flush_standard_output')
    transport('Capital.Output',                     'write_standard_output')
    transport('Capital.Path',                       'path_basename')
    transport('Capital.Path',                       'path_join')
    transport('Capital.Path',                       'path_normalize')
    transport('Capital.Path',                       'read_text_from_path')
    transport('Capital.Path',                       'write_binary_to_path')
    transport('Capital.PortrayString',              'portray_raw_string')
    transport('Capital.PortrayString',              'portray_string')
    transport('Capital.SimpleStringIO',             'create_SimpleStringOutput')
    transport('Capital.Sleep',                      'sleep')
    transport('Capital.StringOutput',               'create_StringOutput')
    transport('Capital.StringOutput',               'StringOutput')
    transport('Capital.System',                     'caller_frame_1')
    transport('Capital.System',                     'change_check_interval')
    transport('Capital.System',                     'fetch_check_interval')
    transport('Capital.System',                     'module_path')
    transport('Capital.System',                     'my_line')
    transport('Capital.System',                     'program_exit')
    transport('Capital.System',                     'python_version')
    transport('Capital.System',                     'slice_all')
    transport('Capital.Thread',                     'allocate_lock')
    transport('Capital.Thread',                     'start_new_thread')
    transport('Capital.Thread',                     'thread_identifier')
    transport('Capital.Traceback',                  'print_exception_chain')
    transport('CoreParser.ActionWord',              'conjure_action_word')
    transport('CoreParser.ActionWord',              'conjure_action_word__ends_in_newline')
    transport('CoreParser.ActionWord',              'conjure_ActionWord_WithNewlines')
    transport('CoreParser.ActionWord',              'initialize_action_word__Meta')
    transport('CoreParser.ActionWord',              'produce_conjure_action_word__ends_in_newline')
    transport('CoreParser.ActionWord',              'produce_conjure_action_word__normal')
    transport('CoreParser.Atom',                    'conjure_double_quote')
    transport('CoreParser.Atom',                    'conjure_name')
    transport('CoreParser.Atom',                    'conjure_single_quote')
    transport('CoreParser.Atom',                    'conjure_token_number')
    transport('CoreParser.Atom',                    'DoubleQuote')
    transport('CoreParser.Atom',                    'lookup_name')
    transport('CoreParser.Atom',                    'produce_conjure_atom')
    transport('CoreParser.Atom',                    'SingleQuote')
    transport('CoreParser.Atom',                    'TokenName')
    transport('CoreParser.BinaryExpression',        'AddExpression')
    transport('CoreParser.BinaryExpression',        'BinaryExpression')
    transport('CoreParser.BinaryExpression',        'conjure_add_expression')
    transport('CoreParser.BinaryExpression',        'produce_conjure_binary_expression')
    transport('CoreParser.BookcaseCoupleTwig',      'BookcaseCoupleTwig')
    transport('CoreParser.BookcaseCoupleTwig',      'produce_conjure_bookcase_couple_twig')
    transport('CoreParser.BookcaseDualTwig',        'BookcaseDualTwig')
    transport('CoreParser.BookcaseDualTwig',        'produce_conjure_bookcase_dual_twig')
    transport('CoreParser.BookcaseExpression',      'BookcaseExpression')
    transport('CoreParser.BookcaseExpression',      'conjure_parenthesized_expression')
    transport('CoreParser.BookcaseExpression',      'conjure_parenthesized_expression__with_frill')
    transport('CoreParser.BookcaseExpression',      'LEFT_PARENTHESIS__RIGHT_PARENTHESIS')
    transport('CoreParser.BookcaseExpression',      'ParenthesizedExpression')
    transport('CoreParser.BookcaseExpression',      'produce_conjure_bookcase_expression')
    transport('CoreParser.ClassOrder',              'CLASS_ORDER__NORMAL_TOKEN')
    transport('CoreParser.ClassOrder',              'CLASS_ORDER__PYTHON_END')
    transport('CoreParser.ClassOrder',              'CLASS_ORDER__PYTHON_START')
    transport('CoreParser.CreateMeta',              'lookup_adjusted_meta')
    transport('CoreParser.CreateMeta',              'store_adjusted_meta')
    transport('CoreParser.CrystalComment',          'conjure_any_comment_line')
    transport('CoreParser.CrystalComment',          'empty_comment_line')
    transport('CoreParser.CrystalIndentation',      'conjure_indentation')
    transport('CoreParser.CrystalIndentation',      'empty_indentation')
    transport('CoreParser.CrystalIndentation',      'next_indentation')
    transport('CoreParser.DualExpressionStatement', 'DualExpressionStatement')
    transport('CoreParser.DualExpressionStatement', 'produce_dual_expression_statement')
    transport('CoreParser.DualFrill',               'conjure_commented_v_frill')
    transport('CoreParser.DualFrill',               'conjure_vw_frill')
    transport('CoreParser.DualToken',               'Atom_Whitespace')
    transport('CoreParser.DualToken',               'conjure_atom_whitespace')
    transport('CoreParser.DualToken',               'conjure_name_whitespace')
    transport('CoreParser.DualToken',               'conjure_whitespace_atom')
    transport('CoreParser.DualToken',               'conjure_whitespace_name')
    transport('CoreParser.DualToken',               'DualToken')
    transport('CoreParser.DualToken',               'evoke_name_whitespace')
    transport('CoreParser.DualToken',               'evoke_whitespace_name')
    transport('CoreParser.DualToken',               'find_evoke_crystal_atom_whitespace')
    transport('CoreParser.DualToken',               'find_evoke_crystal_whitespace_atom')
    transport('CoreParser.DualToken',               'find_evoke_whitespace_atom')
    transport('CoreParser.DualToken',               'Name_Whitespace')
    transport('CoreParser.DualToken',               'produce_conjure_dual_token__line_marker')
    transport('CoreParser.DualToken',               'produce_conjure_dual_token__normal')
    transport('CoreParser.DualToken',               'produce_evoke_dual_token__ends_in_newline')
    transport('CoreParser.DualToken',               'produce_evoke_dual_token__indentation')
    transport('CoreParser.DualToken',               'produce_evoke_dual_token__line_marker')
    transport('CoreParser.DualToken',               'produce_evoke_dual_token__whitespace')
    transport('CoreParser.DualToken',               'Whitespace_Atom')
    transport('CoreParser.DualTwig',                'DualTwig')
    transport('CoreParser.DualTwig',                'produce_conjure_dual_twig')
    transport('CoreParser.DumpToken',               'create_TokenOutput')
    transport('CoreParser.DumpToken',               'dump_all_tokens')
    transport('CoreParser.Elemental',               'conjure_keyword_import')
    transport('CoreParser.Elemental',               'conjure_keyword_import__ends_in_newline')
    transport('CoreParser.Elemental',               'conjure_keyword_language')
    transport('CoreParser.Elemental',               'conjure_left_parenthesis')
    transport('CoreParser.Elemental',               'conjure_left_parenthesis__ends_in_newline')
    transport('CoreParser.Elemental',               'conjure_right_parenthesis')
    transport('CoreParser.Elemental',               'conjure_right_parenthesis__ends_in_newline')
    transport('CoreParser.Elemental',               'is_CRYSTAL_close_or_open_operator')
    transport('CoreParser.Elemental',               'KeywordAndOperatorBase')
    transport('CoreParser.Elemental',               'KeywordImport')
    transport('CoreParser.Elemental',               'LEFT_PARENTHESIS')
    transport('CoreParser.Elemental',               'OperatorLeftParenthesis')
    transport('CoreParser.Elemental',               'OperatorPlusSign')
    transport('CoreParser.Elemental',               'OperatorRightParenthesis')
    transport('CoreParser.Elemental',               'RIGHT_PARENTHESIS')
    transport('CoreParser.EmptyLine',               'conjure_empty_line')
    transport('CoreParser.LineMarker',              'conjure_line_marker')
    transport('CoreParser.LineMarker',              'LINE_MARKER')
    transport('CoreParser.ManyExpression',          'ArithmeticExpression_Many')
    transport('CoreParser.ManyExpression',          'conjure_arithmetic_expression_many')
    transport('CoreParser.ManyExpression',          'conjure_arithmetic_expression_many__with_frill')
    transport('CoreParser.ManyExpression',          'ManyExpression')
    transport('CoreParser.ManyExpression',          'order__frill_many')
    transport('CoreParser.ManyExpression',          'produce_conjure_many_expression')
    transport('CoreParser.ManyExpression',          'scout_variables__many')
    transport('CoreParser.ManyFrill',               'conjure_many_frill')
    transport('CoreParser.Method',                  'construct__123')
    transport('CoreParser.Method',                  'count_newlines__123')
    transport('CoreParser.Method',                  'display_token__123')
    transport('CoreParser.Method',                  'display_token__with_braces')
    transport('CoreParser.Method',                  'find_require_module__0')
    transport('CoreParser.Method',                  'is_name__0')
    transport('CoreParser.Method',                  'mutate__self')
    transport('CoreParser.Method',                  'order__ab')
    transport('CoreParser.Method',                  'order__abc')
    transport('CoreParser.Method',                  'order__frill_a')
    transport('CoreParser.Method',                  'order__frill_ab')
    transport('CoreParser.Method',                  'order__s')
    transport('CoreParser.Method',                  'portray__123')
    transport('CoreParser.Method',                  'portray__ab')
    transport('CoreParser.Method',                  'portray_with_braces')
    transport('CoreParser.Method',                  'produce_mutate__uncommented')
    transport('CoreParser.Method',                  'produce_transform__ab')
    transport('CoreParser.Method',                  'produce_transform__abc')
    transport('CoreParser.Method',                  'produce_transform__abcd')
    transport('CoreParser.Method',                  'produce_transform_many')
    transport('CoreParser.Method',                  'produce_transform__uncommented')
    transport('CoreParser.Method',                  'scout_variables__0')
    transport('CoreParser.Method',                  'scout_variables__a')
    transport('CoreParser.Method',                  'scout_variables__ab')
    transport('CoreParser.Method',                  'scout_variables__b')
    transport('CoreParser.Method',                  'transform__remove_comments_0')
    transport('CoreParser.Method',                  'transform__self')
    transport('CoreParser.Method',                  'Whitespace_Name')
    transport('CoreParser.Method',                  'write_variables__a')
    transport('CoreParser.Nub',                     'conjure_nub')
    transport('CoreParser.Nub',                     'static_conjure_nub')
    transport('CoreParser.ParserToken',             'ParserToken')
    transport('CoreParser.ParserTrunk',             'ParserTrunk')
    transport('CoreParser.QuadrupleFrill',          'conjure_commented_vwx_frill')
    transport('CoreParser.QuadrupleFrill',          'conjure_vwxy_frill')
    transport('CoreParser.QuadrupleTwig',           'produce_conjure_quadruple_twig')
    transport('CoreParser.QuadrupleTwig',           'QuadrupleTwig')
    transport('CoreParser.TestTree',                'test_count_newlines')
    transport('CoreParser.TestTree',                'test_identical_output')
    transport('CoreParser.TokenCache',              'lookup_indentation')
    transport('CoreParser.TokenCache',              'lookup_line_marker')
    transport('CoreParser.TokenCache',              'lookup_normal_token')
    transport('CoreParser.TokenCache',              'provide_indentation')
    transport('CoreParser.TokenCache',              'provide_line_marker')
    transport('CoreParser.TokenCache',              'provide_normal_token')
    transport('CoreParser.TokenizeAtom',            'analyze_CRYSTAL_close_operator')
    transport('CoreParser.TokenizeAtom',            'produce_analyze_LANGUAGE_functions')
    transport('CoreParser.TokenizeAtom',            'produce_analyze_LANGUAGE_newline_close_operator')
    transport('CoreParser.TokenizeOperator',        'produce__LANGUAGE__skip_tokenize_prefix')
    transport('CoreParser.Tokenizer',               'parse_context')
    transport('CoreParser.Tokenizer',               'qd')
    transport('CoreParser.Tokenizer',               'qi')
    transport('CoreParser.Tokenizer',               'qj')
    transport('CoreParser.Tokenizer',               'qk')
    transport('CoreParser.Tokenizer',               'ql')
    transport('CoreParser.Tokenizer',               'qn')
    transport('CoreParser.Tokenizer',               'qs')
    transport('CoreParser.Tokenizer',               'raise_unknown_line')
    transport('CoreParser.Tokenizer',               'wd')
    transport('CoreParser.Tokenizer',               'wd0')
    transport('CoreParser.Tokenizer',               'wd1')
    transport('CoreParser.Tokenizer',               'wi')
    transport('CoreParser.Tokenizer',               'wj')
    transport('CoreParser.Tokenizer',               'wk')
    transport('CoreParser.Tokenizer',               'wn')
    transport('CoreParser.Tokenizer',               'ws')
    transport('CoreParser.Tokenizer',               'z_initialize')
    transport('CoreParser.TokenTuple',              'TokenTuple')
    transport('CoreParser.TripleFrill',             'conjure_commented_vw_frill')
    transport('CoreParser.TripleFrill',             'conjure_vwx_frill')
    transport('CoreParser.TripleToken',             'create_triple_token__line_marker')
    transport('CoreParser.TripleToken',             'create_triple_token__with_newlines')
    transport('CoreParser.TripleToken',             'evoke_whitespace_name_whitespace')
    transport('CoreParser.TripleToken',             'find_evoke_whitespace_atom_whitespace')
    transport('CoreParser.TripleToken',             'produce_evoke_triple_token__ends_in_newline')
    transport('CoreParser.TripleToken',             'produce_evoke_triple_token__line_marker')
    transport('CoreParser.TripleToken',             'TripleToken')
    transport('CoreParser.TripleToken',             'Whitespace_Atom_Whitespace')
    transport('CoreParser.TripleToken',             'Whitespace_Name_Whitespace')
    transport('CoreParser.TripleTwig',              'produce_conjure_triple_twig')
    transport('CoreParser.TripleTwig',              'TripleTwig')
    transport('CoreParser.TupleOfExpression',       'conjure_tuple_of_many_expression')
    transport('CoreParser.Whitespace',              'conjure_whitespace')
    transport('CoreParser.Whitespace',              'conjure_whitespace__ends_in_newline')
    transport('Rex.Compile',                        'compile_regular_expression')
    transport('Rex.Parse',                          'parse_ascii_regular_expression')
