import pytest
from playwright.sync_api import expect
from pages.sandbox_page import SandboxPage

@pytest.fixture(autouse=True)
def setup(page):
    sandbox = SandboxPage(page)
    sandbox.navigate()
    return sandbox

def test_click_boton_id_dinamico(setup):
    setup.dynamic_id_button.click()
    # expect ahora funcionará porque está importado arriba
    expect(setup.dynamic_id_message).to_be_visible()

def test_ingreso_texto_input(setup):
    texto = "Estoy aprendiendo Playwright"
    setup.main_input.fill(texto)
    expect(setup.main_input).to_have_value(texto)

def test_selecciono_checkbox_pasta(setup):
    setup.pasta_checkbox.check()
    expect(setup.pasta_checkbox).to_be_checked()

def test_selecciono_radio_button_si(setup):
    setup.si_radio_button.check()
    expect(setup.si_radio_button).to_be_checked()

def test_selecciono_deporte_tennis_dropdown(setup):
    setup.sports_dropdown.select_option("Tennis")
    expect(setup.sports_dropdown).to_have_value("Tennis")

def test_valido_columna_nombre_tabla_estatica(setup):
    nombres_esperados = ["Messi", "Ronaldo", "Mbappe"]
    nombres_reales = setup.get_static_table_names()
    assert nombres_reales == nombres_esperados

def test_valido_cambio_tabla_dinamica(page, setup):
    valores_antes = setup.get_dynamic_table_values()
    page.reload()
    valores_despues = setup.get_dynamic_table_values()
    assert len(valores_antes) == len(valores_despues)
    for i in range(len(valores_antes)):
        assert valores_antes[i] != valores_despues[i]

def test_validando_popup(setup):
    setup.popup_btn.click()
    expect(setup.popup_text).to_be_visible()
    setup.close_popup_btn.click()