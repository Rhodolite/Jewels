#
#   Copyright (c) 2017-2019 Joy Diamond.  All rights reserved.
#
import  Capital.Builtin                                                 #   Capital.Boot
import  Capital.Privileged                                              #   Capital.Boot
import  Capital.Shared                                                  #   Capital.Boot
import  Python_Exception                                                #   Capital.Boot
import  Python_System                                                   #   Capital.Boot

from    Capital.BuiltIn     import  __build_class                       #   Capital.Boot (Python 3 only)
from    Capital.BuiltIn     import  __import__                          #   Capital.Boot
from    Capital.BuiltIn     import  privileged_2                        #   Capital.Core


    transport('Board.CreateGameBoard',              'create_game_board')
    transport('Board.SquareFoundation',             'SquareFoundation')
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
    transport('Capital.Capital_Object',             'base_classes__Capital_Object')
    transport('Capital.Capital_Object',             'Capital_Object')
    transport('Capital.Capital_Object',             'Capital_Object__operator_new')
    transport('Capital.Capital_Object',             'lookup__hidden_introspection_key')
    transport('Capital.Capital_Object',             'new_instance')
    transport('Capital.Capital_Object',             'Object__operator__delete_attribute')
    transport('Capital.Capital_Object',             'Object__operator__set_attribute')
    transport('Capital.Capital_StringBuilder',      'create_StringBuilder__ALLY__Zone')
    transport('Capital.CatchException',             'catch_AttributeError')
    transport('Capital.CatchException',             'catch_FileNotFoundError')
    transport('Capital.CatchException',             'catch_TypeError')
    transport('Capital.CatchException',             'create_CatchException')
    transport('Capital.Class_FindSymbol',           'conjure__class_members')
    transport('Capital.Class_FindSymbol',           'find_symbol_base_and_depth')
    transport('Capital.Class_FindSymbol',           'produce_find_symbol')
    transport('Capital.Class_ShowMembers',          'show_class_members')
    transport('Capital.Codec',                      'encode_ascii')
    transport('Capital.ContextManager',             'empty_context_manager')
    transport('Capital.Core',                       'address_of')
    transport('Capital.Core',                       'arrange')
    transport('Capital.Core',                       'attribute')
    transport('Capital.Core',                       'Boolean')
    transport('Capital.Core',                       'Bytes')
    transport('Capital.Core',                       'character')
    transport('Capital.Core',                       'class_method')
    transport('Capital.Core',                       'enumerate')
    transport('Capital.Core',                       'execute')
    transport('Capital.Core',                       'false')
    transport('Capital.Core',                       'FrozenSet')
    transport('Capital.Core',                       'Function')
    transport('Capital.Core',                       'globals')
    transport('Capital.Core',                       'hash')
    transport('Capital.Core',                       'Integer')
    transport('Capital.Core',                       'intern_arrange')
    transport('Capital.Core',                       'intern_integer')
    transport('Capital.Core',                       'intern_string')
    transport('Capital.Core',                       'is_instance')
    transport('Capital.Core',                       'is_python_2')
    transport('Capital.Core',                       'is_python_3')
    transport('Capital.Core',                       'is_subclass')
    transport('Capital.Core',                       'iterate')
    transport('Capital.Core',                       'iterate_range')
    transport('Capital.Core',                       'length')
    transport('Capital.Core',                       'line')
    transport('Capital.Core',                       'LiquidSet')
    transport('Capital.Core',                       'List')
    transport('Capital.Core',                       'Long')
    transport('Capital.Core',                       'Map')
    transport('Capital.Core',                       'MapProxy')
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
    transport('Capital.Core',                       'property_3')
    transport('Capital.Core',                       'python_debug_mode')
    transport('Capital.Core',                       'raising_exception')
    transport('Capital.Core',                       'raising_exception_from')
    transport('Capital.Core',                       'rename')
    transport('Capital.Core',                       'rename_function')
    transport('Capital.Core',                       'set_attribute')
    transport('Capital.Core',                       'Slice')
    transport('Capital.Core',                       'sorted_list')
    transport('Capital.Core',                       'sorted_tuple')
    transport('Capital.Core',                       'static_method')
    transport('Capital.Core',                       'String')
    transport('Capital.Core',                       'sum')
    transport('Capital.Core',                       'true')
    transport('Capital.Core',                       'Tuple')
    transport('Capital.Core',                       'type')
    transport('Capital.Core',                       'Type')
    transport('Capital.Create_Metaclass',           'create_metaclass')
    transport('Capital.DelayedFileOutput',          'create_DelayedFileOutput')
    transport('Capital.DumpCache',                  'dump_cache_to_string')
    transport('Capital.DumpCache',                  'print_cache')
    transport('Capital.Exception',                  'AttributeError')
    transport('Capital.Exception',                  'except_any_clause')
    transport('Capital.Exception',                  'except_clause')
    transport('Capital.Exception',                  'Exception')
    transport('Capital.Exception',                  'exit_clause')
    transport('Capital.Exception',                  'FileNotFoundError')
    transport('Capital.Exception',                  'finally_clause')
    transport('Capital.Exception',                  'ImportError')
    transport('Capital.Exception',                  'OSError')
    transport('Capital.Exception',                  'PermissionError')
    transport('Capital.Exception',                  'PREPARE_attribute_ERROR')
    transport('Capital.Exception',                  'PREPARE_runtime_ERROR')
    transport('Capital.Exception',                  'raise_attribute_error')
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
    transport('Capital.Introspection',              'introspect')
    transport('Capital.Introspection',              'introspect_hidden')
    transport('Capital.Line',                       'blank')
    transport('Capital.Line',                       'blank_suppress')
    transport('Capital.Line',                       'change_prefix')
    transport('Capital.Line',                       'indent')
    transport('Capital.Line',                       'output')
    transport('Capital.Map',                        'first_map_item')
    transport('Capital.Map',                        'iterate_items_sorted_by_key')
    transport('Capital.Map',                        'iterate_values_sorted_by_key')
    transport('Capital.Map',                        'values_tuple_sorted_by_key')
    transport('Capital.Map',                        'view_items')
    transport('Capital.Map',                        'view_values')
    transport('Capital.Meta_Metaclass',             'Meta_Metaclass')
    transport('Capital.Method',                     'return_self')
    transport('Capital.Output',                     'flush_standard_output')
    transport('Capital.Output',                     'write_standard_output')
    transport('Capital.Path',                       'path_basename')
    transport('Capital.Path',                       'path_join')
    transport('Capital.Path',                       'path_normalize')
    transport('Capital.Path',                       'path_split')
    transport('Capital.Path',                       'read_text_from_path')
    transport('Capital.Path',                       'remove_path')
    transport('Capital.Path',                       'remove_path__ignore_file_not_found')
    transport('Capital.Path',                       'rename_path')
    transport('Capital.Path',                       'rename_path__ignore_file_not_found')
    transport('Capital.Path',                       'write_binary_to_path')
    transport('Capital.PortrayString',              'portray_raw_string')
    transport('Capital.PortrayString',              'portray_string')
    transport('Capital.ProcessObjectMembers',       'base_classes__Object')
    transport('Capital.ProcessObjectMembers',       'process_object_members')
    transport('Capital.PythonType',                 'portray_builtin_method')
    transport('Capital.PythonType',                 'portray_method_wrapper')
    transport('Capital.PythonType',                 'portray_slot_wrapper')
    transport('Capital.SimpleStringIO',             'create_SimpleStringOutput')
    transport('Capital.Sleep',                      'sleep')
    transport('Capital.StringOutput',               'create_StringOutput')
    transport('Capital.StringOutput',               'StringOutput')
    transport('Capital.System',                     'caller_frame_1')
    transport('Capital.System',                     'change_check_interval')
    transport('Capital.System',                     'fetch_check_interval')
    transport('Capital.System',                     'MAXIMUM_INTEGER')                              #   Python 2.0 only
    transport('Capital.System',                     'module_path')
    transport('Capital.System',                     'my_line')
    transport('Capital.System',                     'program_exit')
    transport('Capital.System',                     'python_version')
    transport('Capital.System',                     'slice_all')
    transport('Capital.Thread',                     'allocate_lock')
    transport('Capital.Thread',                     'start_new_thread')
    transport('Capital.Thread',                     'thread_identifier')
    transport('Capital.Traceback',                  'print_exception_chain')
    transport('Capital.TupleFunctions',             'produce_append_freeze')
    transport('Capital.TupleFunctions',             'produce_append_freeze_zap')
    transport('Capital.TypeMembers',                'create_python_type')
    transport('Capital.TypeMembers',                'Type__operator__call')
    transport('Capital.UniqueName',                 'create_UniqueName')
    transport('Capital.Zone',                       'current_zone')
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
    transport('CoreParser.BookcaseExpression',      'conjure_CRYSTAL_parenthesized_expression')
    transport('CoreParser.BookcaseExpression',      'conjure_CRYSTAL_parenthesized_expression__with_frill')
    transport('CoreParser.BookcaseExpression',      'LEFT_PARENTHESIS__RIGHT_PARENTHESIS')
    transport('CoreParser.BookcaseExpression',      'ParenthesizedExpression')
    transport('CoreParser.BookcaseExpression',      'produce_conjure_bookcase_expression')
    transport('CoreParser.BookcaseManyExpression',  'BookcaseManyExpression')
    transport('CoreParser.BookcaseManyExpression',  'dump_token__X__many')
    transport('CoreParser.BookcaseManyExpression',  'produce_conjure_bookcase_many_expression')
    transport('CoreParser.BookcaseManyExpression',  'write__X__many_end')
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
    transport('CoreParser.Elemental',               'COLON')
    transport('CoreParser.Elemental',               'COLON__W')
    transport('CoreParser.Elemental',               'COMMA__W')
    transport('CoreParser.Elemental',               'conjure_colon')
    transport('CoreParser.Elemental',               'conjure_colon__ends_in_newline')
    transport('CoreParser.Elemental',               'conjure_CRYSTAL_comma')
    transport('CoreParser.Elemental',               'conjure_CRYSTAL_comma__ends_in_newline')
    transport('CoreParser.Elemental',               'conjure_keyword_import')
    transport('CoreParser.Elemental',               'conjure_keyword_import__ends_in_newline')
    transport('CoreParser.Elemental',               'conjure_keyword_language')
    transport('CoreParser.Elemental',               'conjure_left_brace')
    transport('CoreParser.Elemental',               'conjure_left_brace__ends_in_newline')
    transport('CoreParser.Elemental',               'conjure_left_parenthesis')
    transport('CoreParser.Elemental',               'conjure_left_parenthesis__ends_in_newline')
    transport('CoreParser.Elemental',               'conjure_left_square_bracket')
    transport('CoreParser.Elemental',               'conjure_left_square_bracket__ends_in_newline')
    transport('CoreParser.Elemental',               'conjure_right_brace')
    transport('CoreParser.Elemental',               'conjure_right_brace__ends_in_newline')
    transport('CoreParser.Elemental',               'conjure_right_parenthesis')
    transport('CoreParser.Elemental',               'conjure_right_parenthesis__ends_in_newline')
    transport('CoreParser.Elemental',               'conjure_right_square_bracket')
    transport('CoreParser.Elemental',               'conjure_right_square_bracket__ends_in_newline')
    transport('CoreParser.Elemental',               'dump_token__a__frill__braces')
    transport('CoreParser.Elemental',               'dump_token__frill__a__braces')
    transport('CoreParser.Elemental',               'is_CRYSTAL_close_or_open_operator')
    transport('CoreParser.Elemental',               'KeywordAndOperatorBase')
    transport('CoreParser.Elemental',               'KeywordImport')
    transport('CoreParser.Elemental',               'KeywordLanguage')
    transport('CoreParser.Elemental',               'LEFT_BRACE')
    transport('CoreParser.Elemental',               'LEFT_BRACE__RIGHT_BRACE')
    transport('CoreParser.Elemental',               'LEFT_BRACE__W')
    transport('CoreParser.Elemental',               'LEFT_PARENTHESIS')
    transport('CoreParser.Elemental',               'LEFT_SQUARE_BRACKET')
    transport('CoreParser.Elemental',               'LEFT_SQUARE_BRACKET__RIGHT_SQUARE_BRACKET')
    transport('CoreParser.Elemental',               'LEFT_SQUARE_BRACKET__W')
    transport('CoreParser.Elemental',               'OperatorAndSign')
    transport('CoreParser.Elemental',               'OperatorColon')
    transport('CoreParser.Elemental',               'OperatorComma')
    transport('CoreParser.Elemental',               'OperatorGreaterThanSign')
    transport('CoreParser.Elemental',               'OperatorLeftBrace')
    transport('CoreParser.Elemental',               'OperatorLeftParenthesis')
    transport('CoreParser.Elemental',               'OperatorLeftSquareBracket')
    transport('CoreParser.Elemental',               'OperatorOrSign')
    transport('CoreParser.Elemental',               'OperatorPlusSign')
    transport('CoreParser.Elemental',               'OperatorRightBrace')
    transport('CoreParser.Elemental',               'OperatorRightParenthesis')
    transport('CoreParser.Elemental',               'OperatorRightSquareBracket')
    transport('CoreParser.Elemental',               'OperatorSolidus')
    transport('CoreParser.Elemental',               'RIGHT_BRACE')
    transport('CoreParser.Elemental',               'RIGHT_PARENTHESIS')
    transport('CoreParser.Elemental',               'RIGHT_SQUARE_BRACKET')
    transport('CoreParser.Elemental',               'SOLIDUS')
    transport('CoreParser.Elemental',               'W__AND_SIGN__W')
    transport('CoreParser.Elemental',               'W__COLON__W')
    transport('CoreParser.Elemental',               'W__GREATER_THAN_SIGN__W')
    transport('CoreParser.Elemental',               'W__OR_SIGN__W')
    transport('CoreParser.Elemental',               'W__RIGHT_BRACE')
    transport('CoreParser.Elemental',               'W__RIGHT_SQUARE_BRACKET')
    transport('CoreParser.Elemental',               'W__SOLIDUS__W')
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
    transport('CoreParser.Method',                  'display_token__ab__with_braces')
    transport('CoreParser.Method',                  'display_token__with_angle_signs')
    transport('CoreParser.Method',                  'dump_token__with_angle_signs')
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
    transport('CoreParser.ParseAtom',               'produce_parse_LANGUAGE__bookcase_expression')
    transport('CoreParser.ParseExpression',         'produce_parse_LANGUAGE__X_expression__left_operator')
    transport('CoreParser.ParserToken',             'ParserToken')
    transport('CoreParser.ParserTrunk',             'ParserTrunk')
    transport('CoreParser.PostfixExpression',       'PostfixExpression')
    transport('CoreParser.PostfixExpression',       'produce_conjure_postfix_expression')
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
    transport('CoreParser.TripleToken',             'produce_conjure_triple_token__line_marker')
    transport('CoreParser.TripleToken',             'produce_conjure_triple_token__with_newlines')
    transport('CoreParser.TripleToken',             'produce_evoke_triple_token__ends_in_newline')
    transport('CoreParser.TripleToken',             'produce_evoke_triple_token__line_marker')
    transport('CoreParser.TripleToken',             'TripleToken')
    transport('CoreParser.TripleToken',             'Whitespace_Atom_Whitespace')
    transport('CoreParser.TripleToken',             'Whitespace_Name_Whitespace')
    transport('CoreParser.TripleTwig',              'produce_conjure_triple_twig')
    transport('CoreParser.TripleTwig',              'TripleTwig')
    transport('CoreParser.TupleOfExpression',       'conjure_tuple_of_many_expression')
    transport('CoreParser.UnaryExpression',         'AT_SIGN')
    transport('CoreParser.UnaryExpression',         'conjure_twos_complement_expression')
    transport('CoreParser.UnaryExpression',         'OperatorAtSign')
    transport('CoreParser.UnaryExpression',         'OperatorTildeSign')
    transport('CoreParser.UnaryExpression',         'produce_conjure_unary_expression')
    transport('CoreParser.UnaryExpression',         'TILDE_SIGN')
    transport('CoreParser.UnaryExpression',         'TwosComplementExpression')
    transport('CoreParser.UnaryExpression',         'UnaryExpression')
    transport('CoreParser.Whitespace',              'conjure_whitespace')
    transport('CoreParser.Whitespace',              'conjure_whitespace__ends_in_newline')
    transport('Rex.Compile',                        'compile_regular_expression')
    transport('Rex.Parse',                          'parse_ascii_regular_expression')
