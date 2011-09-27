class MarkupBase(object):
    text_enabled_plugins = False
    is_dynamic = False

    def parse(self, value, context=None, placeholder=None):
        """
        This is the main method of the parser. It returns parsed output from a given markup input.

        While parsing it can store internally additional scripts and stylesheets to be retrieved later from the parser object.
        """
        raise NotImplementedError

    def plugin_id_list(self, text):
        """
        Returns the list of plugins inserted and currently used in the markup text.
        """
        return []

    def replace_plugins(self, text, id_dict):
        """
        Replaces references to plugins in the markup text with new ids.
        """
        return text

    def plugin_markup(self):
        """
        Returns JavaScript code for anonymous function which construct plugin markup given plugin_id, icon_src and icon_alt arguments. It should be marked as safe to prevent escaping.
        """
        return None

    def plugin_regexp(self):
        """
        Returns JavaScript code for anonymous function which construct plugin regexp given plugin_id. It should be marked as safe to prevent escaping.
        """
        return None

    def get_scripts(self):
        """
        Returns a list of {href, type} dictionaries for all scripts which should be additionaly loaded.

        They will be inserted at the end of the page.
        """
        return []

    def get_stylesheets(self):
        """
        Returns a list of {href, type} dictionaries for all stylesheets which should be additionally loaded.

        JavaScript code will be added at the end of the page to inject them into the head.
        """
        return []

    def get_plugin_urls(self):
        """
        Returns URL patterns for views used by this plugin.
        """
        return []

class MarkupPluginException(Exception):
    pass
