from playwright.sync_api import Page

class SandboxPage:
    def __init__(self, page: Page):
        self.page = page
        self.dynamic_id_button = page.get_by_role("button", name="Hacé click para generar un ID")
        self.dynamic_id_message = page.get_by_text("OMG, aparezco después de 3 segundos de haber hecho click en el botón 👻.")
        self.main_input = page.get_by_placeholder("Ingresá texto")
        self.pasta_checkbox = page.get_by_role("checkbox", name="Pasta 🍝")
        self.si_radio_button = page.get_by_role("radio", name="Si")
        self.sports_dropdown = page.get_by_label("Dropdown")
        self.popup_btn = page.get_by_role("button", name="Mostrar popup")
        self.popup_text = page.get_by_text("¿Viste? ¡Apareció un Pop-up!")
        self.close_popup_btn = page.get_by_role("button", name="Cerrar")
        
        # Selectores para tablas
        self.static_table_names = 'h2:has-text("Tabla estática") + table tbody tr td:nth-child(2)'
        self.dynamic_table_cells = 'h2:has-text("Tabla dinámica") + table tbody tr td'

    def navigate(self):
        self.page.goto("https://thefreerangetester.github.io/sandbox-automation-testing/")

    def get_static_table_names(self):
        return self.page.eval_on_selector_all(self.static_table_names, "elements => elements.map(e => e.textContent.trim())")

    def get_dynamic_table_values(self):
        return self.page.eval_on_selector_all(self.dynamic_table_cells, "elements => elements.map(e => e.textContent.trim())")