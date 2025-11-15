"""
MkDocs ChatBot Plugin
"""

import os
from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin
from mkdocs.config.defaults import MkDocsConfig
from pathlib import Path


class ChatBotPlugin(BasePlugin):
    """
    MkDocs plugin to add an OpenAI-powered chatbot to documentation pages.
    """

    config_scheme = (
        ('enabled', config_options.Type(bool, default=True)),
        ('api_key', config_options.Type(str, default='')),
        ('api_base_url', config_options.Type(str, default='https://api.openai.com/v1')),
        ('model', config_options.Type(str, default='gpt-4o-mini')),
        ('position', config_options.Type(str, default='bottom-right')),  # bottom-right, bottom-left, top-right, top-left
        ('button_color', config_options.Type(str, default='#3b82f6')),
        ('button_text_color', config_options.Type(str, default='#ffffff')),
        ('chat_title', config_options.Type(str, default='Documentation Assistant')),
        ('placeholder_text', config_options.Type(str, default='Ask me anything about the documentation...')),
        ('welcome_message', config_options.Type(str, default='Hi! I\'m your documentation assistant. How can I help you today?')),
        ('context_pages', config_options.Type(int, default=3)),  # Number of pages to include as context
        ('temperature', config_options.Type(float, default=0.7)),
        ('max_tokens', config_options.Type(int, default=1000)),
        ('system_prompt', config_options.Type(str, default='')),
    )

    def on_config(self, config: MkDocsConfig) -> MkDocsConfig:
        """
        Called when the config is loaded.
        """
        if not self.config['enabled']:
            return config

        # Set default system prompt if not provided
        if not self.config['system_prompt']:
            self.config['system_prompt'] = (
                "You are a helpful assistant for a technical documentation website. "
                "Answer questions based on the documentation content provided. "
                "Be concise, accurate, and helpful. If you don't know something, say so. "
                "Use markdown formatting in your responses."
            )

        return config

    def on_post_page(self, output: str, page, config: MkDocsConfig) -> str:
        """
        Inject chatbot HTML and assets into each page.
        """
        if not self.config['enabled']:
            return output

        # Get the plugin directory
        plugin_dir = Path(__file__).parent

        # Read CSS and JS files
        css_file = plugin_dir / 'assets' / 'chatbot.css'
        js_file = plugin_dir / 'assets' / 'chatbot.js'

        try:
            with open(css_file, 'r', encoding='utf-8') as f:
                chatbot_css = f.read()

            with open(js_file, 'r', encoding='utf-8') as f:
                chatbot_js = f.read()
        except FileNotFoundError as e:
            print(f"Warning: Chatbot asset file not found: {e}")
            return output

        # Generate configuration JavaScript
        config_js = f"""
        <script>
            window.CHATBOT_CONFIG = {{
                apiKey: '{self.config['api_key']}',
                apiBaseUrl: '{self.config['api_base_url']}',
                model: '{self.config['model']}',
                position: '{self.config['position']}',
                buttonColor: '{self.config['button_color']}',
                buttonTextColor: '{self.config['button_text_color']}',
                chatTitle: '{self.config['chat_title']}',
                placeholderText: '{self.config['placeholder_text']}',
                welcomeMessage: '{self.config['welcome_message']}',
                systemPrompt: `{self.config['system_prompt']}`,
                temperature: {self.config['temperature']},
                maxTokens: {self.config['max_tokens']},
                currentPage: {{
                    title: '{page.title}',
                    url: '{page.url}',
                    content: `{self._escape_js_string(page.content if hasattr(page, 'content') else '')}`
                }}
            }};
        </script>
        """

        # Chatbot HTML
        chatbot_html = """
        <!-- MkDocs ChatBot -->
        <div id="mkdocs-chatbot-container">
            <button id="chatbot-toggle-btn" aria-label="Open chat">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
                </svg>
            </button>

            <div id="chatbot-window" class="chatbot-hidden">
                <div class="chatbot-header">
                    <h3 id="chatbot-title"></h3>
                    <button id="chatbot-close-btn" aria-label="Close chat">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <line x1="18" y1="6" x2="6" y2="18"></line>
                            <line x1="6" y1="6" x2="18" y2="18"></line>
                        </svg>
                    </button>
                </div>

                <div id="chatbot-messages" class="chatbot-messages"></div>

                <div class="chatbot-input-container">
                    <textarea
                        id="chatbot-input"
                        rows="1"
                        placeholder=""
                        aria-label="Chat input"
                    ></textarea>
                    <button id="chatbot-send-btn" aria-label="Send message">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <line x1="22" y1="2" x2="11" y2="13"></line>
                            <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
                        </svg>
                    </button>
                </div>
            </div>
        </div>
        """

        # Inject everything before closing body tag
        injection = f"""
        <style>{chatbot_css}</style>
        {config_js}
        {chatbot_html}
        <script>{chatbot_js}</script>
        """

        # Find and inject before </body>
        if '</body>' in output:
            output = output.replace('</body>', f'{injection}</body>')
        else:
            output += injection

        return output

    def _escape_js_string(self, text: str) -> str:
        """
        Escape a string for use in JavaScript.
        """
        return (text
                .replace('\\', '\\\\')
                .replace('`', '\\`')
                .replace('$', '\\$')
                .replace('\n', '\\n')
                .replace('\r', '\\r')
                [:5000])  # Limit content length to avoid huge payloads
