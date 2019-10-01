"""
Dummy weechat python module.
    Purpose:
        To add code completion/documentation/Intellisense for the weechat module
        when editing python weechat scripts in Pycharm/vscode and similar code
        editors. This module is designed for python (3.x) and weechat (> 2.4)
    How To Use:
        Place this module in a location which will allow your python environment
        to import it to satisfy your "import weechat" declaration.
        (Same directory typically will work (python 3+))

        You should now see function names, parameter information and
        documentation when using intellisense features of your editor.
        Function, parameter, examples and other info were stolen liberally
        from : https://weechat.org/files/doc/stable/weechat_plugin_api.en.html
    Version / Revision History:
        1.0 - Initial Version
    Credits:
        Sébastien Helleu flashcode@flashtux.org :
            Scripting API and Plugin API references: https://weechat.org/doc
            which provided function descriptions, argument details, return
            values and examples.
        David Bishop <dbishop38@gmail.com> :
            module assembly with professional cut and paste skills.
"""
# pylint: disable= unused-argument, unnecessary-pass, too-many-lines
# pylint: disable= too-many-arguments

def register(name: str, author: str, version: str, script_license: str,
             description: str, shutdown_function: str, charset: str) -> None:
    """ Registers script in WeeChat.

    :param name: internal name of script
    :param author: authors name
    :param version: script version (ex, "1.0")
    :param script_license: script license (ex, "MIT", "GPL3" )
    :param description: short description of this script
    :param shutdown_function: name of function called when script is unloaded
    :param charset: script charset (default UTF-8)
    :return: None
    """
    pass


def charset_set(charset: str) -> None:
    """ Set new plugin charset (default charset is UTF-8)

    :param str charset: character set to use (ex "UTF-8" or "iso-8859-1")
    :return None: None
    """
    pass


def iconv_to_internal(charset: str, string: str) -> str:
    """ Convert string to WeeChat internal charset (UTF-8).

    :param str charset: target character set
    :param str string: string to convert
    :return str: converted string (must be freed by calling "free")

    .. code-block:: python

        str = weechat.iconv_to_internal("iso-8859-1", "iso string: é à")
    """
    pass


def iconv_from_internal(charset: str, string: str) -> str:
    """ Convert string from internal WeeChat charset (UTF-8) to another.

    :param charset: target character set
    :param string: string to convert
    :return: converted string (must be freed by calling "free"? API only?)

    .. code-block:: python

        str = weechat.iconv_from_internal("iso-8859-1", "utf-8 string: é à")
    """
    pass


def plugin_get_name(plugin: str) -> str:
    """ Gets Plugin name.

    :param plugin: plugin to get name of
    :return: name of plugin

    .. code-block:: python

        plugin = weechat.buffer_get_pointer(weechat.current_buffer(), "plugin")
        name = weechat.plugin_get_name(plugin)
    """
    pass


def gettext(string: str) -> str:
    """ Return translated string (depends on local language).

    :param string: string to translate
    :return: translated string or string if no translation available

    .. code-block:: python

        str = weechat.gettext("hello")
    """
    pass


def ngettext(string: str, plural: str, count: int) -> str:
    """ Return translated string, using single or plural form.

    :param string: string to translate, single form
    :param plural: string to translate, plural form
    :param count: used to choose between single and plural form

    :return: translated string or string if there is no translation available

    .. code-block:: python

        num_files = 2
        str = weechat.ngettext("file", "files", num_files)
    """
    pass


def strlen_screen(string: str) -> int:
    """ Return number of chars needed on screen to display UTF-8 string.

    :param string: string to display
    :return: number of chars needed on screen to display UTF-8 string

    .. code-block:: python

        length = weechat.strlen_screen("é")  # 1

    :Note:

        Non-printable chars have a width of 1
        (this is the difference with the function utf8_strlen_screen).
    """
    pass


def string_match(string: str, mask: str, case_sensitive: int) -> int:
    """ Check if a string matches a mask.

    :param string: string to compare
    :param mask: mask with wildcards (*)
        (each wildcard matches 0 or more chars in the string)
    :param case_sensitive: 1 for case sensitive comparison, otherwise 0
    :return: 1 if string matches mask, otherwise 0

    .. code-block:: python

        match5 = weechat.string_match("abcdef", "*b*d*", 0)  # == 1
    """
    pass


def string_match_list(string: str, masks: str, case_sensitive: int) -> int:
    """ Check if a string matches a list of masks.

    :param string: string to compare
    :param masks: list of masks
        (each mask is compared to the string with the function string_match)
    :param case_sensitive: 1 for case sensitive comparison, otherwise 0
    :return: 1 if string matches list of masks, otherwise 0
        (at least one mask matches and no negative mask matches)

    .. code-block:: python

        match1 = weechat.string_match_list("abc", "*,!abc*", 0)     # == 0
        match2 = weechat.string_match_list("abcdef", "*,!abc*", 0)  # == 0
        match3 = weechat.string_match_list("def", "*,!abc*", 0)     # == 1

    :Notes:

        negative mask is allowed with the format "!word"
        A negative mask has higher priority than a
        standard mask. (Requires Weechat > 2.5)
    """
    pass


def string_eval_path_home(path: str, pointers: dict, extra_vars: dict,
                          options: dict) -> str:
    """ Evaluate a path in 3 steps.

    1. replace leading %h by WeeChat home directory,
    2. replace leading ~ by user home directory (call to string_expand_home),
    3. evaluate variables (see string_eval_expression).

    :param path: path
    :param pointers: hashtable for call to function string_eval_expression
    :param extra_vars: hashtable for call to function string_eval_expression
    :param options: hashtable for call to function string_eval_expression
    :return: evaluated path (must be freed by calling "free")

    .. code-block:: python

        path = weechat.string_eval_path_home("%h/test", {}, {}, {})
        path == "/home/xxx/.weechat/test"
    """
    pass


def string_mask_to_regex(mask: str) -> str:
    """ Return a regex, built with a mask, where only special char is *

    :param mask: str, mask to create a regex for
    :return: str, regular expression

    :Note:

        All other special chars for regex are escaped.

    .. code-block:: python

        regex = weechat.string_mask_to_regex("test*mask")  # "test.*mask"
    """
    pass


def string_has_highlight(string: str, highlight_words: str) -> int:
    """ Check if a string has one or more highlights in list of highlight words.

    :param string: string to check
    :param highlight_words: list of highlight words, separated by comma
    :return: 1 if string has one or more highlights, otherwise 0

    .. code-block:: python

        highlight = weechat.string_has_highlight("my test string", "test,word2")
        # 1
    """
    pass


def string_has_highlight_regex(string: str, regex: str) -> int:
    """ Check if a string has one or more highlights in regex.

    :param string: string to check
    :param regex: POSIX extended regular expressio
    :return: 1 if string has one or more highlights, otherwise 0

    .. note::

        POSIX extended regular expression.
        For at least one match of regular expression on string, it must be
        surrounded by delimiters (chars different from: alphanumeric, - _ | ).

    .. code-block:: python

        highlight = weechat.string_has_highlight_regex(
                        "my test string", "test|word2")  # 1

    """
    pass


def string_format_size(size: int) -> str:
    """ Build a string with formatted file size and a unit.

    :param size: size (in bytes)
    :return: size formatted as text

    .. note:

        Translated to local language

    .. code-block:: python

        # Requires WeeChat > 2.2
        str = weechat.string_format_size(15200)  # == "15.2 KB"

    """
    pass


def string_remove_color(string: str, replacement: str) -> str:
    """ Remove WeeChat colors from a string.

    :param string: string to remove color from
    :param replacement:replaced by first char (removed if null or empty)
    :return: string without color

    .. code-block:: python

        str = weechat.string_remove_color(my_string, "?")
    """
    pass


def string_is_command_char(string: str) -> int:
    """ Check if first char of string is a command char.

    :param string: string to check
    :return: 1 if first char of string is a command char, otherwise 0

    .. note:

        default command char is /

    .. code-block:: python

        command_char1 = weechat.string_is_command_char("/test")  # == 1
    """
    pass


def string_input_for_buffer(string: str) -> str:
    """ Return pointer to input text for buffer.

    :param string: string to check
    :return: pointer into "string", or NULL ("") if it’s a command.

    .. code-block:: python

        str1 = weechat.string_input_for_buffer("test")    # "test"
        str2 = weechat.string_input_for_buffer("/test")   # ""
        str3 = weechat.string_input_for_buffer("//test")  # "/test"
    """


def string_eval_expression(expr: str, pointers: dict, extra_vars: dict,
                           options: dict) -> str:
    """ Evaluate an expression and return result as a string.

    :param expr: the expression to evaluate
    :param pointers: hashtable with pointers (keys = string, values = pointer)
    :param extra_vars: extra variables that will be expanded
    :param options: hashtable with options (keys and values must be string)
    :return: evaluated expression

    .. code-block:: python

        # conditions
            str1 = weechat.string_eval_expression("${window.win_width} > 100",
                                        {}, {}, {"type": "condition"})  # "1"
            str2 = weechat.string_eval_expression("abc =~ def", {}, {},
                                        {"type": "condition"})   # "0"
        # simple expression
            str3 = weechat.string_eval_expression("${buffer.full_name}",
                                        {}, {}, {})   # "core.weechat"
        # replace with regex: add brackets around URLs
            options = {
                "regex": "[a-zA-Z0-9_]+://[^ ]+",
                "regex_replace": "[ ${re:0} ]",
            }
            str4 = weechat.string_eval_expression("test: https://weechat.org",
                        {}, {}, options)   # "test: [ https://weechat.org ]"
        # replace with regex: hide passwords
            options = {
                "regex": "(password=)([^ ]+)",
                "regex_replace": "${re:1}${hide:*,${re:2}}",
            }
            str5 = weechat.string_eval_expression("password=abc password=def",
                                {}, {}, options)  # "password=*** password=***"

    :Note:

        Special variables with format ${variable} are expanded.
        https://weechat.org/files/doc/stable/weechat_plugin_api.en.html#_string_eval_expression

    """
    pass


def mkdir_home(directory: str, mode: int) -> int:
    """ Create a directory in WeeChat home.

    :param directory: directory to create
    :param mode: mode (unix permissions)
    :return: 1 if directory was successfully created, 0 if an error occurred

    .. code-block:: python

            weechat.mkdir_home("temp", 0755)

    """
    pass


def mkdir(directory: str, mode: int) -> int:
    """ Creates a directory.

    :param directory: directory to create
    :param mode: mode (unix permissions)
    :return: 1 if directory was successfully created, 0 if an error occurred

    .. code-block:: python

            weechat.mkdir("/tmp/my_dir/", 0755)

    """
    pass


def mkdir_parents(directory: str, mode: int) -> int:
    """ Creates a directory, creates the parent directories as needed.

    :param directory: directory to create
    :param mode: mode (unix permissions)
    :return:  1 if directory was successfully created, 0 if an error occurred

    .. code-block:: python

            weechat.mkdir("/tmp/my_dir/", 0755)
    """
    pass


def list_new() -> str:
    """ Creates a new weechat list.

    :return: pointer to a new list
    """
    pass


def list_add(the_list: str, data: str, where: int, user_data: str) -> str:
    """ Add an item in a list.

    :param the_list: pointer to a list
    :param data: item to add to the list
    :param where: beginning, end, or stay sorted (weechat constant, see notes)
    :param user_data: any pointer
    :return: pointer to new item

    .. note::
        - WEECHAT_LIST_POS_SORT: add in list, keeping list sorted
        - WEECHAT_LIST_POS_BEGINNING: add to beginning of list
        - WEECHAT_LIST_POS_END: add to end of list

    .. code-block:: python

        item = weechat.list_add(list, "my data",
            weechat.WEECHAT_LIST_POS_SORT, "")
    """
    pass


def list_search(the_list: str, data: str) -> str:
    """ Search list for data.

    :param the_list: pointer to list
    :param data: item to find
    :return: pointer to item found, NULL if item was not found

    .. code-block:: python

        item = weechat.list_search(list, "my data")
    """
    pass


def list_search_pos(the_list: str, data: str) -> int:
    """ Search an item position in a list.

    :param the_list: pointer to list
    :param data: data to search in list
    :return: position of item found, -1 if item was not found

    .. code-block:: python

        pos_item = weechat.list_search_pos(list, "my data")
    """
    pass


def list_casesearch(the_list: str, data: str) -> str:
    """ Search an item in a list, ignoring case.

    :param the_list: pointer to list
    :param data: data to search in list
    :return: pointer to item found, NULL if item was not found

    .. code-block:: python

        item = weechat.list_casesearch(list, "my data")
    """
    pass


def list_casesearch_pos(the_list: str, data: str) -> int:
    """ Search an item position in a list, ignoring case.

    :param the_list: pointer to list
    :param data: data to search in list
    :return: position of item found, -1 if item was not found

    .. code-block:: python
        pos_item = weechat.list_casesearch_pos(list, "my data")
    """
    pass


def list_get(the_list: str, position: int) -> str:
    """ Return an item in a list by position.

    :param the_list: pointer to list
    :param position: position in list(first item is 0)
    :return: pointer to item found, NULL if item was not found.

    .. code-block:: python

        item = weechat.list_get(list, 0)
    """
    pass


def list_set(item: str, value: str):
    """ Set new value for an item.

    :param item: item pointer
    :param value: new value for item
    :return: None

    .. code-block:: python

        weechat.list_set(item, "new_data")

    """
    pass


def list_next(item: str) -> str:
    """ Return next item in list.

    :param item: item pointer
    :return: pointer to next item, NULL if pointer was last item in list

    .. code-block:: python

        item = weechat.list_next(item)
    """
    pass


def list_prev(item: str) -> str:
    """ Return previous item in list.

    :param item: item pointer
    :return: pointer to previous item, NULL if pointer was first item in list

    .. code-block:: python

        item = weechat.list_prev(item)
    """
    pass


def list_string(item: str) -> str:
    """ Return string value of an item.

    :param item: item pointer
    :return: string value of item

    .. code-block:: python

        weechat.prnt("", "value of item: %s" % weechat.list_string(item))
    """
    pass


def list_size(the_list: str) -> int:
    """ Return size of list (number of items).

    :param the_list: list pointer
    :return: size of list (number of items), 0 if list is empty

    .. code-block:: python

        weechat.prnt("", "size of list: %d" % weechat.list_size(list))

    """
    pass


def list_remove(the_list: str, item: str) -> None:
    """ Remove an item in a list.

    :param the_list: list pointer
    :param item: item pointer
    :return: None

    .. code-block:: python

        weechat.list_remove(list, item)
    """
    pass


def list_remove_all(the_list: str) -> None:
    """ Remove all items from a list.

    :param the_list: list pointer
    :return: None

    .. code-block:: python

        weechat.list_remove_all(list)
    """
    pass


def list_free(the_list: str) -> None:
    """ Free a list.

    :param the_list: list pointer
    :return: None

    .. code-block:: python

        weechat.list_free(list)
    """
    pass


def config_new(name: str, callback_reload: str,
               callback_reload_data: str) -> str:
    """ Create a new configuration file.

    :param name: name of configuration file (without path or extension)
    :param callback_reload: called when configuration file is reloaded
                            with /reload (optional, can be "")
    :param callback_reload_data: pointer given to callback
    :return: pointer to new configuration file, NULL ("") if an error occurred

    .. code-block:: python

        def my_config_reload_cb(data, config_file):
            # ...
            return weechat.WEECHAT_RC_OK
        config_file = weechat.config_new("test", "my_config_reload_cb", "")
    """
    pass


def config_new_section(config_file: str, name: str, user_can_add_options: int,
                       user_can_delete_options: int, callback_read: str,
                       callback_read_data: str, callback_write: str,
                       callback_write_data: str, callback_create_option: str,
                       callback_create_option_data: str,
                       callback_delete_option: str,
                       callback_delete_option_data: str) -> str:
    """ Create a new section in configuration file.

    :param config_file: configuration file pointer
    :param name: name of section
    :param user_can_add_options: 1 (can add to section), or 0 if it is forbidden
    :param user_can_delete_options: 1 (can delete), or 0 if it is forbidden
    :param callback_read: pointer to function
        called when option in section is read from disk (usually "" (NULL))
    :param callback_read_data: pointer give to callback (usually "" (NULL))
    :param callback_write: pointer to function
        called when option in section is written in file
    :param callback_write_data: pointer given to callback (usually "" (NULL))
    :param callback_create_option: function called when a new option is created
    :param callback_create_option_data: pointer given to callback (usually "")
    :param callback_delete_option: function called when a option is deleted
    :param callback_delete_option_data: pointer given to callback (usually "")
    :return: pointer to new section in configuration file, "" if error occurred

    .. code-block:: python

            def my_section_read_cb(data, config_file, section,
                                    option_name, value):
                # ...
                return weechat.WEECHAT_CONFIG_OPTION_SET_OK_CHANGED
                # return weechat.WEECHAT_CONFIG_OPTION_SET_OK_SAME_VALUE
                # return weechat.WEECHAT_CONFIG_OPTION_SET_OPTION_NOT_FOUND
                # return weechat.WEECHAT_CONFIG_OPTION_SET_ERROR
            def my_section_write_cb(data, config_file, section_name):
                # ...
                return weechat.WEECHAT_CONFIG_WRITE_OK
            def my_section_write_default_cb(data, config_file, section_name):
                # ...
                return weechat.WEECHAT_CONFIG_WRITE_OK
            def my_section_create_option_cb(data, config_file, section,
                                            option_name, value):
                # ...
                return weechat.WEECHAT_CONFIG_OPTION_SET_OK_SAME_VALUE
            def my_section_delete_option_cb(data, config_file, section, option):
                # ...
                return weechat.WEECHAT_CONFIG_OPTION_UNSET_OK_REMOVED
            section = weechat.config_new_section(config_file, "section1", 1, 1,
                "my_section_read_cb", "",
                "my_section_write_cb", "",
                "my_section_write_default_cb", "",
                "my_section_create_option_cb", "",
                "my_section_delete_option_cb", "")

    """
    pass


def config_search_section(config_file: str, section_name: str) -> str:
    """ Search a section in a configuration file.

    :param config_file: configuration file poimter
    :param section_name: name of section to search
    :return: pointer to section found, NULL if section was not found

    .. code-block:: python

            section = weechat.config_search_section(config_file, "section")
    """
    pass


def config_new_option(config_file: str, section, name, option_type: str,
                      description: str, string_values: str, min_value: int,
                      max_value: int, default_value: str, value: str,
                      null_value_allowed: int, callback_check_value: str,
                      callback_check_value_data: str,
                      callback_change: str, callback_change_data: str,
                      callback_delete: str, callback_delete_data: str) -> str:
    """ Create a new option in a section of a configuration file.

    :param config_file: configuration file pointer
    :param section: pointer to section
    :param name: name of option
    :param option_type: type of option ("boolean", "integer", string" , "color")
    :param description: description of option
    :param string_values: string values (separated by |), used for type integer
    :param min_value: minimum value (for type integer)
    :param max_value: maximum value (for type integer)
    :param default_value: default value (used when option is reset)
    :param value: value for option
    :param null_value_allowed: 1 (NULL) (undefined) allowed, otherwise 0
    :param callback_check_value: function called to check new value for option
    :param callback_check_value_data: pointer given to callback (usually "")
    :param callback_change: function called when value of option has changed
    :param callback_change_data: pointer given to callback (usually "")
    :param callback_delete: function called when option will be deleted
    :param callback_delete_data: pointer given to callback (usually "")
    :return: pointer to new option in section, NULL ("") if error

    .. code-block:: python

        def option4_check_value_cb(data, option, value):
            # ...
            return 1
            # return 0
        def option4_change_cb(data, option):
            # ...
        def option4_delete_cb(data, option):
            # ...
        option1 = weechat.config_new_option(config_file, section,
            "option1", "boolean",
            "My option, type boolean",
            "", 0, 0, "on", "on", 0,
            "", "".
            "", "",
            "", "")

        option2 = weechat.config_new_option(config_file, section,
            "option2", "integer",
            "My option, type integer",
            "", 0, 100, "15", "15", 0,
            "", "",
            "", "",
            "", "")

        option3 = weechat.config_new_option(config_file, section,
            "option3", "integer",
            "My option, type integer (with string values)",
            "top|bottom|left|right",
            0, 0, "bottom", "bottom", 0,
            "", "",
            "", "",
            "", "")

        option4 = weechat.config_new_option(config_file, section,
            "option4", "string",
            "My option, type string",
            "", 0, 0, "test", "test", 1,
            "option4_check_value_cb", "",
            "option4_change_cb", "",
            "option4_delete_cb", "")

        option5 = weechat.config_new_option(config_file, section,
            "option5", "color",
            "My option, type color",
            "", 0, 0, "lightblue", "lightblue", 0,
            "", "",
            "", "",
            "", "")
    """
    pass


def config_search_option(config_file: str, section: str,
                         option_name: str) -> str:
    """ Search an option in a section of a configuration file.

    :param config_file: configuration file pointer
    :param section: section pointer
    :param name: name of option to search
    :return: pointer to option found, NULL if option was not found

    .. code-block:: python

        option = weechat.config_search_option(config_file, section, "option")
    """
    pass


def config_string_to_boolean(text: str) -> int:
    """ Check if a text is "true" or "false", as boolean value.

    :param text: str, text to analyze
    :return: 1 if text is "true" value, 0 if "false" value (see notes)

    .. note::
    - "true" values ("on", "yes", "y", "true", "t", "1")
    - "false" values ("off", "no", "n", "false, "f", "0")

    .. code-block:: python

        if weechat.config_string_to_boolean(text):
            # ...
    """
    pass


def config_option_reset(option: str, run_callback: str) -> int:
    """ Reset an option to its default value.

    :param option: option pointer
    :param run_callback: 1 calls callback if value is changed, otherwise 0
    :return: weechat constant (see notes)

    .. note::
    .   WEECHAT_CONFIG_OPTION_SET_OK_CHANGED if option value has been reset
    .   WEECHAT_CONFIG_OPTION_SET_OK_SAME_VALUE if value was not changed
    .   WEECHAT_CONFIG_OPTION_SET_ERROR if an error occurred

    .. code-block:: python

            rc = weechat.config_option_reset(option, 1)
            if rc == weechat.WEECHAT_CONFIG_OPTION_SET_OK_CHANGED:
                # ...
            elif rc == weechat.WEECHAT_CONFIG_OPTION_SET_OK_SAME_VALUE:
                # ...
            elif rc == weechat.WEECHAT_CONFIG_OPTION_SET_ERROR:
                # ...
    """
    pass


def config_option_set(option: str, value: str, run_callback: int) -> int:
    """ Set new value for an option.

    :param option: option pointer
    :param value: new value for option (see notes)
    :param run_callback: 1 call change callback if value is changed, otherwise 0
    :return:
    - WEECHAT_CONFIG_OPTION_SET_OK_CHANGED if option value has been changed
    - WEECHAT_CONFIG_OPTION_SET_OK_SAME_VALUE if value was not changed
    - WEECHAT_CONFIG_OPTION_SET_ERROR if an error occurred

    .. note::

    special values for "value" are possible:
    - boolean "toggle" toggle the current value
    - integer or color: "++N" add N (any integer) to the current value
                        "--N" subtract N (any integer) from current value
    possible constants for return value:

    .. code-block:: python
        rc = weechat.config_option_set(option, "new_value", 1)
        if rc == weechat.WEECHAT_CONFIG_OPTION_SET_OK_CHANGED:
            # ...
        elif rc == weechat.WEECHAT_CONFIG_OPTION_SET_OK_SAME_VALUE:
            # ...
        elif rc == weechat.WEECHAT_CONFIG_OPTION_SET_ERROR:
            # ...
    """
    pass


def config_option_set_null(option: str, run_callback: int) -> int:
    """ Set null (undefined value) for an option.

    :param option: option pointer
    :param run_callback: 1 call change callback if value is changed, otherwise 0
    :return: WEECHAT_CONFIG_OPTION_SET_* (see notes)

    .. note::
        You can set value to null only if it is allowed for option
            (see config_new_option).
        constants for return value:
        - WEECHAT_CONFIG_OPTION_SET_OK_CHANGED if option value has been changed
        - WEECHAT_CONFIG_OPTION_SET_OK_SAME_VALUE if value was not changed
        - WEECHAT_CONFIG_OPTION_SET_ERROR if an error occurred

    .. code-block:: python

        rc = weechat.config_option_set_null(option, 1)
        if rc == weechat.WEECHAT_CONFIG_OPTION_SET_OK_CHANGED:
            # ...
        elif rc == weechat.WEECHAT_CONFIG_OPTION_SET_OK_SAME_VALUE:
            # ...
        elif rc == weechat.WEECHAT_CONFIG_OPTION_SET_ERROR:
            # ...
    """
    pass


def config_option_unset(option: str) -> int:
    """ unset/reset option.

    :param option: option pointer

    :return: WEECHAT_CONFIG_OPTION_UNSET_OK_NO_RESET
    - WEECHAT_CONFIG_OPTION_UNSET_OK_RESET
    - WEECHAT_CONFIG_OPTION_UNSET_OK_REMOVED
    - WEECHAT_CONFIG_OPTION_UNSET_ERROR

    .. code-block:: python

            rc = weechat.config_option_unset(option)
            if rc == weechat.WEECHAT_CONFIG_OPTION_UNSET_OK_NO_RESET:
                # ...
            elif rc == weechat.WEECHAT_CONFIG_OPTION_UNSET_OK_RESET:
                # ...
            elif rc == weechat.WEECHAT_CONFIG_OPTION_UNSET_OK_REMOVED:
                # ...
            elif rc == weechat.WEECHAT_CONFIG_OPTION_UNSET_ERROR:
                # ...
    """
    pass


def config_option_rename(option: str, new_name: str) -> None:
    """ Rename an option.

    :param option: option pointer
    :param new_name: new name for option
    :return: None

    .. code-block:: python

        weechat.config_option_rename(option, "new_name")
    """
    pass


def config_option_is_null(option: str) -> int:
    """ Check if an option is "null" (undefined value).

    :param option: option pointer
    :return: 1 if value of option is "null", 0 if value of option is not "null"

    .. code-block:: python

        if weechat.config_option_is_null(option):
            # ...
    """
    pass


def config_option_default_is_null(option: str) -> int:
    """ Check if default value for an option is "null" (undefined value).

    :param option: option pointer
    :return: 1 if default value of option is "null" 0 if default is not "null"

    .. code-block:: python

        if weechat.config_option_default_is_null(option):
            # ...
    """
    pass


def config_boolean(option: str) -> int:
    """ Return boolean value of option.

    :param option: option pointer
    :return: option type = boolean: (0 or 1), integer: 0 ,string: 0, color: 0

    .. code-block:: python

        option = weechat.config_get("plugin.section.option")
        if weechat.config_boolean(option):
            # ...

    """
    pass


def config_boolean_default(option: str) -> int:
    """ Return default boolean value of option.

    :param option: option pointer
    :return: option type = boolean: (0 or 1), integer: 0, string: 0, color: 0

    """
    pass


def config_integer(option: str) -> int:
    """ Return integer value of option.

    :param option: option pointer
    :return: option type = boolean: (0 or 1), integer: default integer value,
        string: 0, color: default color index

    """
    pass


def config_integer_default(option: str) -> int:
    """ Return default integer value of option.

    :param option: option pointer
    :return: option type = boolean: (0 or 1)
        integer: default integer value
        string: 0
        color: default color index

    .. code-block:: python

        option = weechat.config_get("plugin.section.option")
        value = weechat.config_integer_default(option)

    """
    pass


def config_string(option: str) -> str:
    """ Return string value of option.

    :param option: option pointer
    :return: depending on option type:
    boolean: "on" if value is true, otherwise "off"
    integer: string value if option is an integer with string values, or NULL
    string: string value of option
    color: name of color

    .. code-block:: python

        option = weechat.config_get("plugin.section.option")
        value = weechat.config_string(option)
    """
    pass


def config_string_default(option: str) -> str:
    """ Return default string value of option.

    :param option: option pointer
    :return: depending on option type:
        boolean: "on" if default value is true, otherwise "off"
        integer: default string value if option is an integer with string values
        string: default string value of option
        color: default name of color

    .. code-block:: python

        option = weechat.config_get("plugin.section.option")
        value = weechat.config_string_default(option)

    """
    pass


def config_color(option: str) -> str:
    """ Return color value of option.

    :param option: option pointer
    :return: depending on option type:
        boolean: NULL ("")
        integer: NULL ("")
        string: NULL ("")
        color: name of color`

    .. code-block:: python

        option = weechat.config_get("plugin.section.option")
        value = weechat.config_color(option)
    """
    pass


def config_color_default(option: str) -> str:
    """ Return default color value of option.

    :param option: str, option pointer
    :return: depending on option type:
        boolean: NULL ("")
        integer: NULL ("")
        string: NULL ("")
        color: default name of color

    .. code-block:: python

        option = weechat.config_get("plugin.section.option")
        value = weechat.config_color(option)
    """
    pass


def config_write_option(config_file: str, option: str) -> None:
    """ Write a line in a configuration file with option and its value.

    :param config_file: configuration file pointer
    :param option: option pointer
    :return: None

    .. note:: this function should be called only in "write" or
        "write_default" callbacks for a section).

    .. code-block:: python

        def my_section_write_cb(data, config_file, section_name):
            weechat.config_write_line(config_file, "my_section", "")
            weechat.config_write_option(config_file, option)
            return weechat.WEECHAT_RC_OK

    """
    pass


def config_write_line(config_file: str, option_name: str, value: str) -> None:
    """ Write a line in a configuration file.

    :param config_file: configuration file pointer
    :param option_name: option name
    :param value: value (if NULL, then line with section name is written,
        for example: "[section]")
    :return: None

    .. note:: (this function should be called only in "write" or
        "write_default" callbacks for a section)

    .. code-block:: python

        def my_section_write_cb(data, config_file, section_name):
            weechat.config_write_line(config_file, "my_section", "")
            weechat.config_write_line(config_file, "option", "value")
            return weechat.WEECHAT_RC_OK
"""
    pass


def config_write(config_file: str) -> int:
    """ Write configuration file to disk.

    :param config_file: configuration file pointer
    :return: WEECHAT_CONFIG_WRITE_OK if configuration was written
        WEECHAT_CONFIG_WRITE_MEMORY_ERROR if there was not enough memory
        WEECHAT_CONFIG_WRITE_ERROR if another error occurred

    .. code-block:: python

        rc = weechat.config_write(config_file)
        if rc == weechat.WEECHAT_CONFIG_WRITE_OK:
            # ...
        elif rc == weechat.WEECHAT_CONFIG_WRITE_MEMORY_ERROR:
            # ...
        elif rc == weechat.WEECHAT_CONFIG_WRITE_ERROR:
            # ...
    """
    pass


def config_read(config_file: str) -> int:
    """ Read configuration file from disk.

    :param config_file: configuration file pointer
    :return: WEECHAT_CONFIG_READ_OK if configuration was loaded
        WEECHAT_CONFIG_READ_MEMORY_ERROR if there was not enough memory
        WEECHAT_CONFIG_READ_FILE_NOT_FOUND if file was not found

    .. code-block:: python

        rc = weechat.config_read(config_file)
        if rc == weechat.WEECHAT_CONFIG_READ_OK:
            # ...
        elif rc == weechat.WEECHAT_CONFIG_READ_MEMORY_ERROR:
            # ...
        elif rc == weechat.WEECHAT_CONFIG_READ_FILE_NOT_FOUND:
            # ...
    """
    pass


def config_reload(config_file: str) -> int:
    """ Reload configuration file from disk.

    :param config_file: configuration file pointer
    :return: WEECHAT_CONFIG_READ_OK if configuration was loaded
        WEECHAT_CONFIG_READ_MEMORY_ERROR if there was not enough memory
        WEECHAT_CONFIG_READ_FILE_NOT_FOUND if file was not found

    .. code-block:: python

        rc = weechat.config_reload(config_file)
        if rc == weechat.WEECHAT_CONFIG_READ_OK:
            # ...
        elif rc == weechat.WEECHAT_CONFIG_READ_MEMORY_ERROR:
            # ...
        elif rc == weechat.WEECHAT_CONFIG_READ_FILE_NOT_FOUND:
            # ...
    """
    pass


def config_option_free(option: str) -> None:
    """ Free an option.

    :param option: option pointer
    :return: None

    .. code-block:: python

        weechat.config_option_free(option)

    """
    pass


def config_section_free_options(section: str) -> None:
    """ Free all options in a section.

    :param section: section pointer
    :return: None

    .. code-block:: python

        weechat.config_section_free_options(section)
    """
    pass


def config_section_free(section: str) -> None:
    """ Free a section.

    :param section: section pointer
    :return: None

    .. code-block:: python

        weechat.config_section_free(section)
    """
    pass


def config_free(section: str) -> None:
    """ Free a configuration file.

    :param section: configuration file pointer
    :return: None

    .. code-block:: python

        weechat.config_free(config_file)
    """
    pass


def config_get(option_name: str) -> str:
    """ Search an option with full name.

    :param option_name: full option name (format: "file.section.option")
    :return: pointer to option found, NULL if option was not found

    .. code-block:: python

        option = weechat.config_get("weechat.look.item_time_format")

    """
    pass


def config_get_plugin(options_name: str) -> str:
    """ Search an option in plugins configuration file (plugins.conf).

    :param options_name: option name
        (WeeChat will add prefix "plugins.var.xxx."
        where "xxx" is current plugin name)
    :return: value of option found, NULL if option was not found

    .. code-block:: python

        value = weechat.config_get_plugin("option")
    """
    pass


def config_is_set_plugin(option_name: str) -> int:
    """ Check if option is set in plugins configuration file (plugins.conf).

    :param option_name: option name (WeeChat will add prefix "plugins.var.xxx."
        where "xxx" is current plugin name)
    :return: 1 if option is set, 0 if option does not exist

    .. code-block:: python

        if weechat.config_is_set_plugin("option"):
            # option is set
            # ...
        else:
            # option does not exist
            # ...
    """
    pass


def config_set_plugin(option_name: str, value: str) -> int:
    """ Set new value for option in plugins configuration file (plugins.conf).

    :param option_name: option name (WeeChat will add prefix "plugins.var.xxx."
        where "xxx" is current plugin name)
    :param value: new value for option
    :return: WEECHAT_CONFIG_OPTION_SET_OK_CHANGED if option value changed
        WEECHAT_CONFIG_OPTION_SET_OK_SAME_VALUE if value was not changed
        WEECHAT_CONFIG_OPTION_SET_OPTION_NOT_FOUND if option was not found
        WEECHAT_CONFIG_OPTION_SET_ERROR if other error occurred

    .. code-block:: python

        rc = weechat.config_set_plugin("option", "test_value")
        if rc == weechat.WEECHAT_CONFIG_OPTION_SET_OK_CHANGED:
            # ...
        elif rc == weechat.WEECHAT_CONFIG_OPTION_SET_OK_SAME_VALUE:
            # ...
        elif rc == weechat.WEECHAT_CONFIG_OPTION_SET_OPTION_NOT_FOUND:
            # ...
        elif rc == weechat.WEECHAT_CONFIG_OPTION_SET_ERROR:
            # ...
    """
    pass


def config_set_desc_plugin(option_name: str, description: str) -> None:
    """ Set description for option in plugins configuration file (plugins.conf).

    :param option_name: option name (WeeChat will add prefix "plugins.desc.xxx."
        where "xxx" is current plugin name)
    :param description: description for option
    :return: None

    .. note:
        It is not a problem if option (plugins.var.xxx.option_name) does not
        exist.
        A future creation of option with this name will use this description.

    .. code-block:: python

        version = weechat.info_get("version_number", "") or 0
        if int(version) >= 0x00030500:
            weechat.config_set_desc_plugin("option", "description of option")
    """
    pass


def config_unset_plugin(option_name: str) -> int:
    """ Unset option in plugins configuration file (plugins.conf)

    :param option_name: option name (WeeChat will add prefix "plugins.var.xxx."
        where xxx is current plugin name)
    :return: WEECHAT_CONFIG_OPTION_UNSET_OK_NO_RESET if value has not been reset
        WEECHAT_CONFIG_OPTION_UNSET_OK_RESET if option value has been reset
        WEECHAT_CONFIG_OPTION_UNSET_OK_REMOVED if option has been removed
        WEECHAT_CONFIG_OPTION_UNSET_ERROR if an error occurred

    .. code-block:: python

        rc = weechat.config_unset_plugin("option")
        if rc == weechat.WEECHAT_CONFIG_OPTION_UNSET_OK_NO_RESET:
            # ...
        elif rc == weechat.WEECHAT_CONFIG_OPTION_UNSET_OK_RESET:
            # ...
        elif rc == weechat.WEECHAT_CONFIG_OPTION_UNSET_OK_REMOVED:
            # ...
        elif rc == weechat.WEECHAT_CONFIG_OPTION_UNSET_ERROR:
            # ...
    """
    pass


def key_bind(context: str, keys: dict) -> int:
    """ Add new key bindings.

    :param context: context for keys:
        "default" : default context (common actions)
        "search" : search context (when searching text in buffer)
        "cursor" : free movement of cursor on screen
        "mouse" : keys for mouse events

    :param keys: hashtable with key bindingsit can contain special keys:
        "__quiet" : do not display the keys added in core buffer (WeeChat ≥ 1.8)
    :return: number of key bindings added

    .. note:
        Unlike command /key bind, this function will never change an existing
        key binding, only new keys are created. To remove a key binding,
        use key_unbind.

    .. code-block:: python

        keys = {"@chat(python.test):button1": "hsignal:test_mouse",
                "@chat(python.test):wheelup": "/mycommand up",
                "@chat(python.test):wheeldown": "/mycommand down"}
        weechat.key_bind("mouse", keys)

    """
    pass


def key_unbind(context: str, key: str) -> int:
    """ Remove key binding(s)

    :param context: context for keys (see key_bind)
    :param key: key to remove or a special value:
        "area:XXX" to remove all keys having XXX as first or second area;
        if the key starts with "quiet:", the keys removed are not
        displayed in core buffer (WeeChat ≥ 2.0).
    :return: number of key bindings removed

    .. note::
        When calling this function, ensure that you will not remove a user
        key binding.

    .. code-block:: python

        # remove a single key
        weechat.key_unbind("mouse", "@chat(plugin.buffer):button1")

        # remove all keys with area "chat(python.test)"
        weechat.key_unbind("mouse", "area:chat(python.test)")
    """

    pass


def prefix(prefix_name: str) -> str:
    """ Return a prefix.

    :param prefix_name: name of prefix
    :return: prefix value (string with prefix and color codes)
        (empty string if not found)

    .. note::
        Values and colors can be customized with command /set.
        defaults:
            error   - "=!="  - yellow     - Error message.
            network - "--"   - magenta    - Message from network.
            action  - "*"    - white      - Self action.
            join    - "-->"  - lightgreen - Someone joins current chat.
            quit    - "<--"  - lightred   - Someone leaves current chat.

    .. code-block:: python

        weechat.prnt("", "%sThis is an error..." % weechat.prefix("error"))
    """
    pass


def color(color_name: str) -> str:
    """ Return a string color code for display.

    :param color_name: name of color, can also be one of:
        1. WeeChat color option name (from weechat.color.xxx),
            for example "chat_delimiters"
        2. option name (format: file.section.option),
            for example "irc.color.message_quit" (WeeChat ≥ 1.2)
        3. color with optional attributes/background (see below)
        attribute:
                bold: set bold
                -bold: remove bold
                reverse: set reverse
                -reverse: remove reverse
                italic: set italic
                -italic: remove italic
                underline: set underline
                -underline: remove underline
                emphasis: toggle the emphasis for text
                    (note: this should be used only in bars, because WeeChat
                    uses text emphasis when searching text in buffer)
                    (WeeChat ≥ 0.4.2)
            bar color name:
                bar_fg: foreground color for bar
                bar_delim: delimiters color for bar
                bar_bg: background color for bar
            reset:
                reset: reset color and attributes
                resetcolor: reset color (keep attributes) (WeeChat ≥ 0.3.6)
            Format of color is:
                attributes (optional) + color name + ",background" (optional).
            Possible attributes are:
                *: bold text
                !: reverse video
                /: italic
                _: underlined text
                |: keep attributes: do not reset bold/reverse/italic/underlined
                    when changing color (WeeChat ≥ 0.3.6)
            Examples:
                yellow: yellow
                _green: underlined green
                *214: bold orange
                yellow,red: yellow on red
                |cyan: cyan (and keep any attribute which was set previously

    :return: string with color code, or an empty string if color is not found

    .. code-block:: python

        weechat.prnt("", "Color: %sblue %sdefault color %syellow on red"
                    % (weechat.color("blue"), weechat.color("chat"),
                    weechat.color("yellow,red")))

    """
    pass


def prnt(buffer: str, message: str) -> None:
    """ Display a message on a buffer.

    :param buffer: buffer pointer, if "", message is displayed on WeeChat buffer
    :param message: message to display
    :return: None

    .. note:
        The first tabulation in message ("\t") is used to separate prefix from
        message. If your message has some tabs and if you don’t want prefix,
        then use a space, a tab, then message (see example below)
        this will disable prefix (the space before tab will not be displayed)

    .. code-block:: python

        weechat.prnt("", "Hello on WeeChat buffer")
        weechat.prnt(buffer, "Hello on this buffer")
        weechat.prnt(buffer, "%sThis is an error!" % weechat.prefix("error"))
        weechat.prnt(buffer, " \tMessage without prefix but with \t some \t tabs")
        weechat.prnt(buffer, "\t\tMessage without time/alignment")
        weechat.prnt(buffer, "\t\t")  # empty line (without time)

    """
    pass


def prnt_date_tags(buffer: str, date: int, tags: str, message: str) -> None:
    """ Display a message on a buffer, using a custom date and tags.

    :param buffer: buffer pointer, if "", message is displayed on WeeChat buffer
    :param date: date for message (0 means current date/time)
    :param tags: comma separated list of tags (NULL ("") means no tags)
    :param message: message to display
    :return: None

    .. code-block:: python

        time = int(time.time())
        weechat.prnt_date_tags("", time - 120, "notify_message",
            "Message 2 minutes ago, with a tag 'notify_message'")
    """
    pass


def prnt_y(buffer: str, y: int, message: str) -> None:
    """ Display a message on a line of a buffer with free content.

    :param buffer: buffer pointer
    :param y: line number (first line is 0)
        a negative value adds a line after last line displayed
        absolute value of y is the number of lines after last line
        (for example -1 is immediately after last line, -2 is 2 lines after
        last line) (WeeChat ≥ 1.0)
    :param message: message to display
    :return: None

    .. code-block:: python

        weechat.prnt_y("", 2, "My message on third line")

    """
    pass


def log_print(message: str) -> None:
    """ Write a message in WeeChat log file (weechat.log).

    :param message: message to write
    :return: None

    .. code-block:: python

        weechat.log_print("My message in log file")
    """
    pass


def hook_command(command: str, description: str, args: str,
                 args_description: str, completion: str, callback: str,
                 callback_data: str) -> str:
    """ Hook a command.

    :param command: command name (priority allowed)
    :param description: description for command (displayed with /help)
    :param args: arguments for command (displayed with /help)
    :param args_description: description of arguments (displayed with /help)
    :param completion: completion template for command
    :param callback: function called when command is used
    :param callback_data: pointer given to callback when it is called by WeeChat
    :return: pointer to new hook

    .. note:: more information :
        https://weechat.org/files/doc/stable/weechat_plugin_api.en.html#_hook_command

    .. code-block:: python

        def my_command_cb(data, buffer, args):
            # ...
            return weechat.WEECHAT_RC_OK

        hook = weechat.hook_command("myfilter", "description of myfilter",
            "[list] | [enable|disable|toggle [name]] | \
            [add name plugin.buffer tags regex] | [del name|-all]",
            "description of arguments...",
            "list"
            " || enable %(filters_names)"
            " || disable %(filters_names)"
            " || toggle %(filters_names)"
            " || add %(filters_names) %(buffers_plugins_names)|*"
            " || del %(filters_names)|-all",
            "my_command_cb", "")

    """
    pass


def hook_completion(completion_item: str, description: str, callback: str,
                    callback_data: str) -> str:
    """ Hook a completion.

    :param completion_item: name of completion item
        after you can use %(name) (or %(name:arguments) with WeeChat ≥ 1.7)
        in a command hooked (argument completion) (priority allowed)
    :param description: description of completion
    :param callback: function calle when completion item is used
    :param callback_data: pointer given to callback, usually ("")

    ..note::
        https://weechat.org/files/doc/stable/weechat_plugin_api.en.html#_hook_completion

    .. code-block:: python

        def my_completion_cb(data, completion_item, buffer, completion):
            weechat.hook_completion_list_add(completion, "word1", 0,
                                             weechat.WEECHAT_LIST_POS_SORT)
            weechat.hook_completion_list_add(completion, "test_word2", 0,
                                             weechat.WEECHAT_LIST_POS_SORT)
        return weechat.WEECHAT_RC_OK

        hook = weechat.hook_completion("plugin_item", "my custom completion!",
                               "my_completion_cb", "")

    """
    pass


def hook_compleetion_list_add(completion: str, word: str, nick_completion: int,
                              where: str) -> None:
    """ Add a word for a completion

    :param completion: completion pointer
    :param word: word to add
    :param nick_completion: 1 if word is a nick, otherwise 0
    :param where: position where word will be inserted in list:
    - WEECHAT_LIST_POS_SORT: any position, to keep list sorted
    - WEECHAT_LIST_POS_BEGINNING: beginning of list
    - WEECHAT_LIST_POS_END: end of list
    :return: None

    """
    pass


def hook_completion_get_string(completion: str, property_name: str) -> str:
    """ Gets a completion property as string.

    :param completion: completion pointer
    :param property_name: property name
    :return: string value of completion property

    .. code-block:: python

        def my_completion_cb(data, completion_item, buffer, completion):
            # get arguments of command
            args = weechat.hook_completion_get_string(completion, "args")
            # completion depending on args
            # ...
            return weechat.WEECHAT_RC_OK

    """
    pass


def hook_command_run(command: str, callback: str, callback_data: str) -> str:
    """ Hook a command when WeeChat runs it.

    :param command: command to hook (wildcard * is allowed) (priority allowed)
    :param callback: function called when command is run
    :param callback_data: pointer given to callback when it is called by WeeChat
    :return: pointer to new hook

    .. code-block:: python

        def my_command_run_cb(data, buffer, command):
            weechat.prnt("", "I'm eating the completion!")
            return weechat.WEECHAT_RC_OK_EAT

        hook = weechat.hook_command_run("/input complete*",
                                        "my_command_run_cb", "")

    """
    pass


def hook_timer(interval: int, align_second: int, max_calls: int, callback: str,
               callback_data: str) -> str:
    """ Hook a timer.

    :param interval: interval between two calls (milliseconds)
    :param align_second: alignment on a second.
        For example:
            if current time is 09:00, if interval = 60000 (60 seconds), and
            align_second = 60, then timer is called each minute when second is 0
    :param max_calls: number of calls to timer (if 0 then timer has no end)
    :param callback: function called when timer is reached
    :param callback_data: pointer given to callback when it is called by WeeChat
    :return: pointer to new hook

    .. code-block:: python

        def my_timer_cb(data, remaining_calls):
        # ...
        return weechat.WEECHAT_RC_OK

        # timer called each 20 seconds
        hook = weechat.hook_timer(20 * 1000, 0, 0, "my_timer_cb", "")

    """
    pass


def hook_fd(fd: str, flag_read: int, flag_write: int, flag_exception: int,
            callback: str, callback_data: str) -> str:
    """ Hook a file descriptor.

    :param fd: file descriptor
    :param flag_read: 1 = catch read event, 0 = ignore
    :param flag_write: 1 = catch write event, 0 = ignore
    :param flag_exception: (WeeChat ≥ 1.3: this argument is ignored)
    :param callback: function called when selected event occurs (file or socket)
    :param callback_data: pointer given to callback when it is called by WeeChat
    :return: pointer to new hook

    .. code-block:: python

        def my_fd_cb(data, fd):
            # ...
            return weechat.WEECHAT_RC_OK

        sock = ...
        hook = weechat.hook_fd(sock, 1, 0, 0, "my_fd_cb", "")

    """
    pass


def hook_process(command: str, timeout: int, callback: str,
                 callback_data: str) -> str:
    """ Hook a process (launched with fork) and catch output)

    :param command: command to launch in a child process. URL or function
    :param timeout: timeout for command (in milliseconds), after this timeout,
        child process is killed (0 = no timeout)
    :param callback: function called when data from child is available, or
        when child has ended.
    :param callback_data: pointer given to callback when it is called by WeeChat
    :return: pointer to new hook

    .. code-block:: python

        # example with an external command
        def my_process_cb(data, command, return_code, out, err):
            if return_code == weechat.WEECHAT_HOOK_PROCESS_ERROR:
                weechat.prnt("", "Error with command '%s'" % command)
                return weechat.WEECHAT_RC_OK
            if return_code >= 0:
                weechat.prnt("", "return_code = %d" % return_code)
            if out != "":
                weechat.prnt("", "stdout: %s" % out)
            if err != "":
                weechat.prnt("", "stderr: %s" % err)
            return weechat.WEECHAT_RC_OK

        hook = weechat.hook_process("ls", 5000, "my_process_cb", "")

        # example with a script function
        def get_status(data):
            # do something blocking...
            # ...
            return "this is the result"

        def my_process_cb(data, command, return_code, out, err):
            if return_code == weechat.WEECHAT_HOOK_PROCESS_ERROR:
                weechat.prnt("", "Error with command '%s'" % command)
                return weechat.WEECHAT_RC_OK
            if return_code >= 0:
                weechat.prnt("", "return_code = %d" % return_code)
            if out != "":
                weechat.prnt("", "stdout: %s" % out)
            if err != "":
                weechat.prnt("", "stderr: %s" % err)
            return weechat.WEECHAT_RC_OK

        hook = weechat.hook_process("func:get_status", 5000, "my_process_cb", "")

    """
    pass


def hook_process_hashtable(command: str, options: dict, timeout: int,
                           callback: str, callback_data: str) -> str:
    """ Hook a process (launched with fork) using options in a hashtable

    :param command: command to launch in a child process. URL or function
    :param options: options for command executed
    :param timeout: timeout for command (in milliseconds), after this timeout,
        child process is killed (0 = no timeout)
    :param callback: function called when data from child is available, or
        when child has ended.
    :param callback_data: pointer given to callback when it is called by WeeChat
    :return: pointer to new hook

    .. note::

    https://weechat.org/files/doc/stable/weechat_plugin_api.en.html#_hook_process
        for extra options available for command "url:...",
        also "man curl_easy_setopt) for description.

    .. code-block:: python

        # example
        def my_process_cb(data, command, return_code, out, err):
            if return_code == weechat.WEECHAT_HOOK_PROCESS_ERROR:
                weechat.prnt("", "Error with command '%s'" % command)
                return weechat.WEECHAT_RC_OK
            if return_code >= 0:
                weechat.prnt("", "return_code = %d" % return_code)
            if out != "":
                weechat.prnt("", "stdout: %s" % out)
            if err != "":
                weechat.prnt("", "stderr: %s" % err)
            return weechat.WEECHAT_RC_OK

        # example 1: download URL
        hook1 = weechat.hook_process_hashtable("url:https://weechat.org/",
                                        {"file_out": "/tmp/weechat.org.html"},
                                        20000, "my_process_cb", "")

        # example 2: open URL with custom HTTP headers
        options = {
            "httpheader": "\n".join([
                "Header1: value1",
                "Header2: value2",
            ]),
        }
        hook2 = weechat.hook_process_hashtable("url:http://localhost:8080/",
                                            options,
                                            20000, "my_process_cb", "")

        # example 3: execute a notify program with a message from someone
        hook3 = weechat.hook_process_hashtable("my-notify-command",
                                            {"arg1": "-from",
                                                "arg2": nick,
                                                "arg3": "-msg",
                                                "arg4": message},  # untrusted
                                            20000, "my_process_cb", "")

        # example 4: call shell to execute a command (command must be SAFE)
        hook4 = weechat.hook_process_hashtable("sh",
                                    {"arg1": "-c",
                                        "arg2": "ls -l /tmp | grep something"},
                                    20000, "my_process_cb", "")

    """
    pass


def hook_connect(proxy: str, address: str, port: int, ipv6: int, retry: int,
                 local_hostname: str, callback: str, callback_data: str) -> str:
    """ Hook a connection (background connection to a remote host).

    :param proxy: name of proxy to use for connection (optional, "" = no proxy)
    :param port: port number
    :param ipv6: 1 to use IPv6, with fallback to IPv4, 0 use only IPv4
    :param retry: retry count, used to fallback to IPv4 (failed connect)
    :param local_hostname: ocal hostname to use for connection (optional)
    :param callback: function called when connection is OK or failed.
    :param callback_data: pointer given to callback
    :return: pointer to new hook

    .. code-block:: python

        def my_connect_cb(data, status, gnutls_rc, sock, error, ip_address):
            if status == WEECHAT_HOOK_CONNECT_OK:
                # ...
            elif status == WEECHAT_HOOK_CONNECT_ADDRESS_NOT_FOUND:
                # ...
            elif status == WEECHAT_HOOK_CONNECT_IP_ADDRESS_NOT_FOUND:
                # ...
            elif status == WEECHAT_HOOK_CONNECT_CONNECTION_REFUSED:
                # ...
            elif status == WEECHAT_HOOK_CONNECT_PROXY_ERROR:
                # ...
            elif status == WEECHAT_HOOK_CONNECT_LOCAL_HOSTNAME_ERROR:
                # ...
            elif status == WEECHAT_HOOK_CONNECT_GNUTLS_INIT_ERROR:
                # ...
            elif status == WEECHAT_HOOK_CONNECT_GNUTLS_HANDSHAKE_ERROR:
                # ...
            elif status == WEECHAT_HOOK_CONNECT_MEMORY_ERROR:
                # ...
            elif status == WEECHAT_HOOK_CONNECT_TIMEOUT:
                # ...
            elif status == WEECHAT_HOOK_CONNECT_SOCKET_ERROR:
                # ...
            return weechat.WEECHAT_RC_OK

        hook = weechat.hook_connect("", "my.server.org", 1234, 1, 0, "",
                                    "my_connect_cb", "")

    """
    pass


def hook_line(buffer_type: str, buffer_name: str, tags: str, callback: str,
              callback_data: str) -> str:
    """ Hook a line to be printed in a buffer.

    :param buffer_type: Catch lines on the given buffer type
        - "formatted" : catch lines on formatted buffers only (default)
        - "free" : catch lines on buffers with free content only
        - "*" : catch lines on all buffer types
    :param buffer_name: comma-separated list of buffer masks
        (see buffer_match_list); NULL, empty string or "*" matches any buffer
    :param tags: catch only messages with these tags (optional):
        comma-separated list of tags that must be in message (logical "or");
        it is possible to combine many tags as a logical "and" with
        separator +; wildcard * is allowed in tags
    :param callback: function called when a line is added in a buffer
    :param callback_data: pointer given in callback when it is called by WeeChat
    :return: pointer to new hook

    .. note::
        When a line is printed in a buffer, hooks are called in this order:
            * hook line (this hook): it can change the buffer, prefix, message,
                tags, notify level, … (see below)
            * hook modifier "weechat_print": it can change the prefix and
                message on a buffer with formatted content
            * hook print: called when the line has been added in a buffer
                with formatted content (nothing can be changed directly
                with this hook).

    .. code-block:: python
    
        def my_line_cb(data, line):
            # force a highlight on the line
            return {"highlight": "1"}

        # catch lines with tag "irc_join"
        hook = weechat.hook_line("", "", "irc_join", "my_line_cb", "")

    """
    pass


def hook_prnt(buffer: str, tags: str, message: str, strip_colors: int,
              callback: str, callback_data: str) -> str:
    """ Hook a message printed.

    :param buffer: buffer pointer, if NULL, messages from any buffer are caught
    :param tags: catch only messages with these tags (optional)
    :param message: only messages with this string will be caught
        (optional, case insensitive)
    :param strip_colors: if 1, colors will be stripped from message displayed,
        before calling callback
    :param callback: function called when a message is printed
    :param callback_data: pointer given to callback when it is called by WeeChat
    :return: pointer to new hook

    .. code-block:: python

        def my_print_cb(data, buffer, date, tags, displayed, highlight,
                        prefix, message):
            if int(highlight):
                # ...
            return weechat.WEECHAT_RC_OK

        # catch all messages, on all buffers, without color
        hook = weechat.hook_print("", "", "", 1, "my_print_cb", "")

    """
    pass

def hook_signal(signal: str, callback: str, callback_data: str) -> str:
    """ Hook a signal

    :param signal: signal to catch, wildcard * is allowed (priority allowed)
    :param callback: function called when signal is received
    :param callback_data: pointer given to callback (usually "")
    :return: pointer to new hook

.. note::

    List of signals:
    signal                  arguments               short description
    ===========================================================================
    guile_script_loaded     path to script          scheme script loaded
    guile_script_unloaded   path to script          scheme script unloaded
    guile_script_installed  csv list of paths       script(s) installed
    guile_script_removed    csv list of scripts     script(s) removed
    xxx,irc_in_yyy          message                 IRC message from server
    xxx,irc_in2_yyy         message                 IRC message (after use)
    xxx,irc_raw_in_yyy      message                 raw IRC msg (all)
    xxx,irc_raw_in2_yyy     message                 raw IRC msg (after use)
    xxx,irc_out_yyy         message                 IRC message sent to server
    xxx,irc_out1_yyy        message                 IRC msg sent before split
    xxx,irc_outtags_yyy     message                 Tags + IRC msg sent
    irc_ctcp                message                 CTCP received
    irc_dcc                 message                 New DCC
    irc_pv                  message                 private message received
    irc_channel_opened      buffer                  Channel msg buffer opened
    irc_pv_opened           buffer                  Private msg buffer opened
    irc_server_opened       buffer                  Server buffer opened
    irc_server_connecting   server name             Connecting to server
    irc_server_connected    server name             Connected to server
    irc_server_disconnected server name             Disconnected from server
    irc_server_lag_changed  server name             Lag changed on the server
    irc_ignore_removing     pointer: ignore         Removing ignore
    irc_ignore_removed                              Ignore removed
    irc_notify_join         server + "," + nick     nick in notify list joined
    irc_notify_quit         server + "," + nick     nick in notify list quit
    irc_notify_away         server + "," + nick     nick in notify list away
                            + "," + away msg
    irc_notify_still_away   server + "," + nick     nick away msg changed
                            + "," + away msg
    irc_notify_back         server + "," + nick     nick in notify list is back
    javascript_script_installed  csv list of paths       script(s) installed
    javascript_script_loaded     path to script          script loaded
    javascript_script_unloaded   path to script          script unloaded
    javascript_script_removed    csv list of scripts     script(s) removed
    logger_start            buffer                  start logging for buffer
    logger_stop             buffer                  stop logging for buffer
    logger_backlog          buffer                  display backlock for buffer
    lua_script_loaded       path to script          lua script loaded
    lua_script_unloaded     path to script          lua script unloaded
    lua_script_installed    csv list of paths       script(s) installed
    lua_script_removed      csv list of scripts     script(s) removed
    perl_script_loaded      path to script          perl script loaded
    perl_script_unloaded    path to script          perl script unloaded
    perl_script_installed   csv list of paths       script(s) installed
    perl_script_removed     csv list of scripts     script(s) removed
    php_script_loaded       path to script          php script loaded
    php_script_unloaded     path to script          php script unloaded
    php_script_installed    csv list of paths       script(s) installed
    php_script_removed      csv list of scripts     script(s) removed
    python_script_loaded    path to script          python script loaded
    python_script_unloaded  path to script          python script unloaded
    python_script_installed csv list of paths       script(s) installed
    python_script_removed   csv list of scripts     script(s) removed
    relay_client_connecting Pointer: relay client   A relay client is connecting
	relay_client_waiting_auth Pointer: relay client Waiting for authentication
    relay_client_auth_ok    Pointer: relay client   Successful authentication
    relay_client_connected  Pointer: relay client   A relay client is connected
    relay_client_auth_failed          relay client  Authentication failed
    relay_client_disconnected  relay client         A relay client disconnected
    ruby_script_loaded      path to script          ruby script loaded
    ruby_script_unloaded    path to script          ruby script unloaded
    ruby_script_installed   csv list of paths       script(s) installed
    ruby_script_removed     csv list of scripts     script(s) removed
    spell_suggest           buffer                  New spelling suggestions
    tcl_script_loaded       path to script          perl script loaded
    tcl_script_unloaded     path to script          perl script unloaded
    tcl_script_installed    csv list of paths       script(s) installed
    tcl_script_removed      csv list of scripts     script(s) removed
    buffer_opened           Pointer: buffer         Buffer opened
    buffer_closing          Pointer: buffer         Closing buffer
    buffer_closed           Pointer: buffer         Buffer closed
    buffer_cleared          Pointer: buffer         Buffer cleared
    buffer_filters_enabled  Pointer: buffer         Filters enabled in buffer
    buffer_filters_disabled Pointer: buffer         Filters disabled in buffer
    buffer_hidden           Pointer: buffer         Buffer hidden
    buffer_unhidden         Pointer: buffer         Buffer unhidden
    buffer_line_added       Pointer: line           Line added in a buffer
    buffer_lines_hidden     Pointer: buffer         Lines hidden in buffer
    buffer_localvar_added   Pointer: buffer         Local variable added
    buffer_localvar_changed Pointer: buffer         Local variable has changed
    buffer_localvar_removed Pointer: buffer         Local variable removed
    buffer_merged           Pointer: buffer         Buffer merged
    buffer_unmerged         Pointer: buffer         Buffer unmerged
    buffer_moved            Pointer: buffer         Buffer moved
    buffer_renamed          Pointer: buffer         Buffer renamed
    buffer_switch           Pointer: buffer         Switching buffer
    buffer_title_changed    Pointer: buffer         Title of buffer changed
    buffer_type_changed     Pointer: buffer         Type of buffer changed
    buffer_zoomed           Pointer: buffer         Merged buffer zoomed
    buffer_unzoomed         Pointer: buffer         Merged buffer unzoomed
    day_changed             new date, format: "2010-01-31"
    debug_dump              String: plugin name     Dump request
    debug_libs              -                   Display external libraries used
    filter_added            Pointer: filter         Filter added
    filter_removing         Pointer: filter         Removing filter
    filter_removed          -                       Filter removed
    filters_enabled         -                       Filters enabled
    filters_disabled        -                       Filters disabled
    hotlist_changed         buffer (can be NULL)    Hotlist changed
    input_paste_pending     -                       Paste pending
    input_search            Pointer: buffer         Text search in buffer
    input_text_changed      Pointer: buffer         Input text changed
    input_text_cursor_moved Pointer: buffer         Input text cursor moved
    key_bind                String: key             Key added
    key_unbind              String: key             Key removed
    key_pressed             String: key pressed     Key pressed
    key_combo_default       String: key combo       Key combo in default context
    key_combo_search        String: key combo       Key combo in search context
    key_combo_cursor        String: key combo       Key combo in cursor context
    mouse_enabled           -                       Mouse enabled
    mouse_disabled          -                       Mouse disabled
    nicklist_group_added    String: buffer pointer  Group added in nicklist
                            + "," + group name.
    nicklist_group_changed  String: buffer pointer  Group changed in nicklist
                            + "," + group name
    nicklist_group_removing String: buffer pointer  Removing group from nicklist
                            + "," + group name
	nicklist_group_removed  String: buffer pointer  Group removed
                            + "," + group name
    nicklist_nick_added     String: buffer pointer  Nick added in nicklist
                            + "," + nick name
    nicklist_nick_changed   String: buffer pointer  Nick changed in nicklist
                            + "," + nick name
    nicklist_nick_removing  String: buffer pointer  Removing nick from nicklist
                            + "," + nick name
    nicklist_nick_removed   String: buffer pointer  Nick removed from nicklist
    	                    + "," + nick name
    partial_completion      -                       Partial completion happened
    plugin_loaded           path to plugin loaded   Plugin loaded
    plugin_unloaded         String: name of plugin unloaded (example: "irc")
    quit                    arguments for /quit     Command /quit issued by user
    signal_sighup           -                       Signal SIGHUP received
    signal_sigquit          -                       Signal SIGQUIT received
    signal_sigterm          -                       Signal SIGTERM received
                                                     (graceful termination)
    signal_sigwinch         -                       Signal SIGWINCH received
                                                    (terminal was resized)
    upgrade                 String: "quit" if       /upgrade issued by user
                            "-quit" argument was
                            given for /upgrade,
                             otherwise NULL.
    upgrade_ended           -                       End of upgrade process
    weechat_highlight       message with prefix     Highlight happened
    weechat_pv              message with prefix     Private message displayed
    window_closing          Pointer: window         Closing window
    window_closed           Pointer: window         Window closed
    window_opened           Pointer: window         Window opened
    window_scrolled         Pointer: window         Scroll in window
    window_switch           Pointer: window         Switching window
    window_zoom             current window          Zooming window
    window_zoomed           current window          Window zoomed
    window_unzoom           current window          Unzooming window
    window_unzoomed         current window          Window unzoomed
    xfer_add                infolist with xfer info     New xfer
    xfer_send_ready         infolist with xfer info     Xfer ready
    xfer_accept_resume      infolist with xfer info     Accept xfer resume
    xfer_send_accept_resume infolist with xfer info     Xfer resumed
    xfer_start_resume       infolist with xfer info     Start resume
    xfer_resume_ready       infolist with xfer info     Xfer resume ready
    xfer_ended              infolist with xfer info     Xfer has ended
    """
    pass

def hook_signal_send(signal: str, type_data: str, signal_data: str) -> int:
    """ Send a signal

    :param signal: signal to send
    :param type_data: type of data sent with signal (see hook_signal)
    :param signal_data: data sent with signal
    :return: return code of last callback executed

    .. note::

        <language>_script_install signal (python, perl, lua, etc) installs
        scripts:
        1. Unload and remove installed script.
        2. Move new script to directory ~/.weechat/xxx/ (where xxx is language)
        3. Create link to new script in directory ~/.weechat/xxx/autoload/
            (only if the script was already auto-loaded,
           or if the option script.scripts.autoload is enabled for a new script)
        4. Load new script (if the script was loaded).
            <language>_script_remove signal (python, perl, lua, etc) installs
            scripts:
        1. each script in list the callback will unload and remove the script.

        Argument is a string with path to script

        irc_input_send can be sent to simulate input in an irc buffer.
        Argument is a string with following format:
            internal server name (required)
            semicolon
            channel name (optional)
            semicolon
            comma-separated list of options (optional):
                priority_high: queue with high priority (like user messages);
                    this is the default priority
                priority_low: queue with low priority
                    (like messages automatically sent by WeeChat)
                user_message: force user message (don’t execute a command)
            semicolon
            comma-separated list of tags used when sending message (optional)
            semicolon
            text or command (required)

    .. code-block:: python

        # say "Hello!" on freenode server, #weechat channel
        weechat.hook_signal_send("irc_input_send",
                        weechat.WEECHAT_HOOK_SIGNAL_STRING,
                        "freenode;#weechat;priority_high,user_message;;Hello!")
        # send command "/whois FlashCode" on freenode server, with low priority
        weechat.hook_signal_send("irc_input_send",
                         weechat.WEECHAT_HOOK_SIGNAL_STRING,
                         "freenode;;priority_low;;/whois FlashCode")
        # unload and remove scripts test.py and script.py
        weechat.hook_signal_send("python_script_remove",
                                 WEECHAT_HOOK_SIGNAL_STRING,
                                 "test.py,script.py")
        # install script test.py
        weechat.hook_signal_send("python_script_install",
                                 WEECHAT_HOOK_SIGNAL_STRING,
                                 "/home/xxx/.weechat/test.py")

    """
    pass


def hook_hsignal(signal: str, callback: str, callback_data: str) -> str:
    """ Hook a hsignal (signal with a hashtable)

    :param signal: signal to catch, wildcard * is allowed (priority allowed)
    :param callback: funciton called when signal is received
    :param callback_data: pointer given to callback (usually "")
    :return: pointer to new hook

    .. note::


    .. code-block:: python

        def my_hsignal_cb(data, signal, hashtable):
            # ...
            return weechat.WEECHAT_RC_OK

        hook = weechat.hook_hsignal("test", "my_hsignal_cb", "")
    """
    pass

def hook_hsignal_send(signal: str, hashtable: dict) -> str:
    """ Send a hsignal (signal with a hashtable/dict)

    :param signal: signal to send
    :param hashtable: hashtable/dict
    :return: return code of last callback executed

    .. code-block:: python

        rc = weechat.hook_hsignal_send("my_hsignal", {"key": "value"})

    """
    pass

def hook_config(option: str, callback: str, callback_data: str) -> str:
    """ Hook a configuration option

    :param option: option, wildcard * is allowed, priority is allowed
    :param callback: function called when configuration option changed
    :param callback_data: pointer given to callback
    :return: pointer to new hook

    .. code-block:: python
        def my_config_cb(data, option, value):
            # ...
            return weechat.WEECHAT_RC_OK
        # catch changes to option "weechat.look.item_time_format"
        hook = weechat.hook_config("weechat.look.item_time_format",
                                   "my_config_cb", "")

    """
    pass

def hook_modifier(modifier: str, callback: str, callback_data: str) -> str:
    """ Hook a modifier

    :param modifier: modifier name
    :param callback: function called when modifier is used
    :param callback_data: pointer sent to callback
    :return: pointer to new hook


    .. code-block:: python

        def my_modifier_cb(data, modifier, modifier_data, string):
            return "%s xxx" % string

        hook = weechat.hook_modifier("weechat_print", "my_modifier_cb", "")

    """
    pass

def hook_modifier_exec(modifier: str, modifier_data: str, string: str) -> str:
    """ Execute modifier(s)

    :param modifier: modifier name
    :param modifier_data: modifier data
    :param string: string to modify
    :return: string modified, NULL ("") if error occurred

    .. code-block: python

        weechat.hook_modifier_exec("my_modifier", my_data, my_string)
    """
    pass

def hook_info(info_name: str, description: str, args_description: str,
              callback: str, callback_data: str) -> str:
    """ Hook an information (callback takes and returns a string)

    :param info_name: name of info (priority allowed)
    :param description: description
    :param args_description: description of arguments (can be NULL "")
    :param callback: function called when info is asked
    :param callback_data: poitner given to callback when it is called
    :return: pointer to new hook

    .. code-block:: python

        def my_info_cb(data, info_name, arguments):
                       return "some_info"

        hook = weechat.hook_info("my_info", "Some info", "Info about arguments",
                                 "my_info_cb", "")

    """
    pass




# CONSTANTS FOR WEECHAT
# (values from weechat-plugin.h but for our purposes shouldn't matter)
WEECHAT_RC_OK = 0
WEECHAT_RC_OK_EAT = 1
WEECHAT_RC_ERROR = -1
WEECHAT_CONFIG_READ_OK = 0
WEECHAT_CONFIG_READ_MEMORY_ERROR = -1
WEECHAT_CONFIG_READ_FILE_NOT_FOUND = -2
WEECHAT_CONFIG_WRITE_OK = 0
WEECHAT_CONFIG_WRITE_ERROR = -1
WEECHAT_CONFIG_WRITE_MEMORY_ERROR = -2
WEECHAT_CONFIG_OPTION_SET_OK_CHANGED = 2
WEECHAT_CONFIG_OPTION_SET_OK_SAME_VALUE = 1
WEECHAT_CONFIG_OPTION_SET_ERROR = 0
WEECHAT_CONFIG_OPTION_SET_OPTION_NOT_FOUND = -1
WEECHAT_CONFIG_OPTION_UNSET_OK_NO_RESET = 0
WEECHAT_CONFIG_OPTION_UNSET_OK_RESET = -1
WEECHAT_CONFIG_OPTION_UNSET_OK_REMOVED = -2
WEECHAT_CONFIG_OPTION_UNSET_ERROR = -1
WEECHAT_LIST_POS_SORT = "sort"
WEECHAT_LIST_POS_BEGINNING = "beginning"
WEECHAT_LIST_POS_END = "end"
WEECHAT_HOTLIST_LOW = "0"
WEECHAT_HOTLIST_MESSAGE = "1"
WEECHAT_HOTLIST_PRIVATE = "2"
WEECHAT_HOTLIST_HIGHLIGHT = "3"
WEECHAT_HOOK_PROCESS_RUNNING = -1
WEECHAT_HOOK_PROCESS_ERROR = -2
WEECHAT_HOOK_CONNECT_OK = 0
WEECHAT_HOOK_CONNECT_ADDRESS_NOT_FOUND = 1
WEECHAT_HOOK_CONNECT_IP_ADDRESS_NOT_FOUND = 2
WEECHAT_HOOK_CONNECT_CONNECTION_REFUSED = 3
WEECHAT_HOOK_CONNECT_PROXY_ERROR = 4
WEECHAT_HOOK_CONNECT_LOCAL_HOSTNAME_ERROR = 5
WEECHAT_HOOK_CONNECT_GNUTLS_INIT_ERROR = 6
WEECHAT_HOOK_CONNECT_GNUTLS_HANDSHAKE_ERROR = 7
WEECHAT_HOOK_CONNECT_MEMORY_ERROR = 8
WEECHAT_HOOK_CONNECT_TIMEOUT = 9
WEECHAT_HOOK_CONNECT_SOCKET_ERROR = 10
WEECHAT_HOOK_SIGNAL_STRING = "string"
WEECHAT_HOOK_SIGNAL_INT = "int"
WEECHAT_HOOK_SIGNAL_POINTER = "pointer"
