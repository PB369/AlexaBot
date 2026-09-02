import webbrowser
from urllib.parse import quote_plus
import asyncio
from playwright.async_api import async_playwright
from playwright._impl._errors import TargetClosedError

# def abrir_youtube(tema):

#     if not tema:
#         return False

#     tema = tema.strip()

#     url = (
#         "https://www.youtube.com/results?search_query="
#         + quote_plus(tema)
#     )

#     return webbrowser.open_new_tab(url)

async def pesquisar_e_abrir_video(tema):

    async with async_playwright() as p:

        navegador = await p.chromium.launch(
            headless=False
        )

        pagina = await navegador.new_page()

        try:

            # Abre o YouTube
            await pagina.goto(
                "https://www.youtube.com",
                wait_until="domcontentloaded",
                timeout=30000
            )

            # Localiza a caixa de pesquisa
            campo_pesquisa = pagina.locator(
                'input[name="search_query"]'
            ).first

            await campo_pesquisa.wait_for(
                state="visible",
                timeout=15000
            )

            # Digita o tema
            await campo_pesquisa.fill(tema)

            print(f"Pesquisando no YouTube: {tema}")

            # Pesquisa usando Enter
            await campo_pesquisa.press("Enter")

            # Espera os resultados
            primeiro_video = pagina.locator(
                "ytd-video-renderer"
            ).first

            await primeiro_video.wait_for(
                state="visible",
                timeout=15000
            )

            # Obtém o título
            titulo = await primeiro_video.locator(
                "#video-title"
            ).get_attribute("title")

            print(
                f"Primeiro vídeo encontrado: {titulo}"
            )

            # Abre o primeiro vídeo
            await primeiro_video.locator(
                "#video-title"
            ).click()

            print("Vídeo aberto com sucesso.")

            # Aguarda um pouco para o vídeo carregar
            await pagina.wait_for_timeout(3000)

            print(
                "YouTube aberto. "
                "Você pode fechar o navegador quando quiser."
            )

            # Mantém o Playwright vivo enquanto a página existir
            try:

                await pagina.wait_for_event(
                    "close"
                )

            except TargetClosedError:

                pass

            print("Navegador do YouTube foi fechado.")

            return True

        except TargetClosedError:

            # Usuário fechou o navegador manualmente
            print(
                "Navegador do YouTube foi fechado pelo usuário."
            )

            return True

        except Exception as erro:

            print(
                f"Erro ao abrir vídeo no YouTube: {erro}"
            )

            return False


def abrir_youtube(tema):

    if not tema:
        return False

    return asyncio.run(
        pesquisar_e_abrir_video(tema)
    )