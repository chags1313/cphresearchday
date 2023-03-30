import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="CPH: Novel UE Movement",
    page_icon="⌚",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

"""
[![forthebadge](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNDEuNTUiIGhlaWdodD0iMzUiIHZpZXdCb3g9IjAgMCAxNDEuNTUgMzUiPjxyZWN0IGNsYXNzPSJzdmdfX3JlY3QiIHg9IjAiIHk9IjAiIHdpZHRoPSIxNDEuNTUiIGhlaWdodD0iMzUiIGZpbGw9IiNBMUExQTEiLz48cmVjdCBjbGFzcz0ic3ZnX19yZWN0IiB4PSIxNDEuNTUiIHk9IjAiIHdpZHRoPSIwIiBoZWlnaHQ9IjM1IiBmaWxsPSIjNkZDMkRFIi8+PHBhdGggY2xhc3M9InN2Z19fdGV4dCIgZD0iTTE1Ljc4IDIyTDE0LjMxIDIyTDE0LjMxIDEzLjQ3TDE1Ljc4IDEzLjQ3TDE1Ljc4IDIyWk0yMi4wNyAyMkwyMC41OSAyMkwyMC41OSAxMy40N0wyMi4wNyAxMy40N0wyNS44OSAxOS41NEwyNS44OSAxMy40N0wyNy4zNiAxMy40N0wyNy4zNiAyMkwyNS44OCAyMkwyMi4wNyAxNS45NUwyMi4wNyAyMlpNMzMuNzggMTQuNjZMMzEuMTQgMTQuNjZMMzEuMTQgMTMuNDdMMzcuOTEgMTMuNDdMMzcuOTEgMTQuNjZMMzUuMjUgMTQuNjZMMzUuMjUgMjJMMzMuNzggMjJMMzMuNzggMTQuNjZaTTQzLjE1IDIyTDQxLjY3IDIyTDQxLjY3IDEzLjQ3TDQ0LjY3IDEzLjQ3UTQ2LjE0IDEzLjQ3IDQ2Ljk1IDE0LjEzUTQ3Ljc1IDE0Ljc5IDQ3Ljc1IDE2LjA1TDQ3Ljc1IDE2LjA1UTQ3Ljc1IDE2LjkwIDQ3LjM0IDE3LjQ4UTQ2LjkyIDE4LjA2IDQ2LjE5IDE4LjM3TDQ2LjE5IDE4LjM3TDQ4LjEwIDIxLjkyTDQ4LjEwIDIyTDQ2LjUxIDIyTDQ0LjgwIDE4LjcxTDQzLjE1IDE4LjcxTDQzLjE1IDIyWk00My4xNSAxNC42Nkw0My4xNSAxNy41Mkw0NC42NyAxNy41MlE0NS40MiAxNy41MiA0NS44NSAxNy4xNVE0Ni4yNyAxNi43NyA0Ni4yNyAxNi4xMUw0Ni4yNyAxNi4xMVE0Ni4yNyAxNS40MyA0NS44OCAxNS4wNVE0NS40OSAxNC42OCA0NC43MiAxNC42Nkw0NC43MiAxNC42Nkw0My4xNSAxNC42NlpNNTEuODggMTguMDBMNTEuODggMTguMDBMNTEuODggMTcuNTJRNTEuODggMTYuMjggNTIuMzIgMTUuMzJRNTIuNzYgMTQuMzcgNTMuNTcgMTMuODZRNTQuMzcgMTMuMzUgNTUuNDEgMTMuMzVRNTYuNDYgMTMuMzUgNTcuMjYgMTMuODVRNTguMDcgMTQuMzUgNTguNTEgMTUuMjlRNTguOTUgMTYuMjMgNTguOTUgMTcuNDhMNTguOTUgMTcuNDhMNTguOTUgMTcuOTZRNTguOTUgMTkuMjEgNTguNTIgMjAuMTZRNTguMDkgMjEuMTAgNTcuMjggMjEuNjFRNTYuNDggMjIuMTIgNTUuNDMgMjIuMTJMNTUuNDMgMjIuMTJRNTQuMzkgMjIuMTIgNTMuNTggMjEuNjFRNTIuNzcgMjEuMTAgNTIuMzIgMjAuMTdRNTEuODggMTkuMjMgNTEuODggMTguMDBaTTUzLjM2IDE3LjQ2TDUzLjM2IDE3Ljk2UTUzLjM2IDE5LjM2IDUzLjkxIDIwLjEzUTU0LjQ1IDIwLjkwIDU1LjQzIDIwLjkwTDU1LjQzIDIwLjkwUTU2LjQxIDIwLjkwIDU2Ljk0IDIwLjE1UTU3LjQ3IDE5LjQwIDU3LjQ3IDE3Ljk2TDU3LjQ3IDE3Ljk2TDU3LjQ3IDE3LjUxUTU3LjQ3IDE2LjA5IDU2LjkzIDE1LjM0UTU2LjQwIDE0LjU4IDU1LjQxIDE0LjU4TDU1LjQxIDE0LjU4UTU0LjQ1IDE0LjU4IDUzLjkxIDE1LjMzUTUzLjM3IDE2LjA5IDUzLjM2IDE3LjQ2TDUzLjM2IDE3LjQ2Wk02NS44NyAyMkw2My40MiAyMkw2My40MiAxMy40N0w2NS45NCAxMy40N1E2Ny4wNyAxMy40NyA2Ny45NCAxMy45N1E2OC44MiAxNC40OCA2OS4zMCAxNS40MFE2OS43OCAxNi4zMyA2OS43OCAxNy41Mkw2OS43OCAxNy41Mkw2OS43OCAxNy45NVE2OS43OCAxOS4xNiA2OS4zMCAyMC4wOFE2OC44MSAyMS4wMCA2Ny45MiAyMS41MFE2Ny4wMyAyMiA2NS44NyAyMkw2NS44NyAyMlpNNjQuOTAgMTQuNjZMNjQuOTAgMjAuODJMNjUuODcgMjAuODJRNjcuMDMgMjAuODIgNjcuNjYgMjAuMDlRNjguMjggMTkuMzYgNjguMjkgMTcuOTlMNjguMjkgMTcuOTlMNjguMjkgMTcuNTJRNjguMjkgMTYuMTMgNjcuNjkgMTUuNDBRNjcuMDkgMTQuNjYgNjUuOTQgMTQuNjZMNjUuOTQgMTQuNjZMNjQuOTAgMTQuNjZaTTc0LjExIDE5LjE2TDc0LjExIDE5LjE2TDc0LjExIDEzLjQ3TDc1LjU5IDEzLjQ3TDc1LjU5IDE5LjE4UTc1LjU5IDIwLjAzIDc2LjAyIDIwLjQ4UTc2LjQ2IDIwLjkzIDc3LjMwIDIwLjkzTDc3LjMwIDIwLjkzUTc5LjAxIDIwLjkzIDc5LjAxIDE5LjEzTDc5LjAxIDE5LjEzTDc5LjAxIDEzLjQ3TDgwLjQ5IDEzLjQ3TDgwLjQ5IDE5LjE3UTgwLjQ5IDIwLjUzIDc5LjYyIDIxLjMyUTc4Ljc1IDIyLjEyIDc3LjMwIDIyLjEyTDc3LjMwIDIyLjEyUTc1LjgzIDIyLjEyIDc0Ljk3IDIxLjMzUTc0LjExIDIwLjU1IDc0LjExIDE5LjE2Wk04NC43OSAxOC4xOUw4NC43OSAxOC4xOUw4NC43OSAxNy4zOVE4NC43OSAxNi4xOSA4NS4yMiAxNS4yN1E4NS42NCAxNC4zNSA4Ni40NCAxMy44NVE4Ny4yNCAxMy4zNSA4OC4yOSAxMy4zNUw4OC4yOSAxMy4zNVE4OS43MCAxMy4zNSA5MC41NiAxNC4xMlE5MS40MyAxNC44OSA5MS41NyAxNi4yOUw5MS41NyAxNi4yOUw5MC4wOSAxNi4yOVE4OS45OCAxNS4zNyA4OS41NSAxNC45NlE4OS4xMiAxNC41NSA4OC4yOSAxNC41NUw4OC4yOSAxNC41NVE4Ny4zMiAxNC41NSA4Ni44MSAxNS4yNlE4Ni4yOSAxNS45NiA4Ni4yOCAxNy4zM0w4Ni4yOCAxNy4zM0w4Ni4yOCAxOC4wOVE4Ni4yOCAxOS40NyA4Ni43NyAyMC4yMFE4Ny4yNyAyMC45MiA4OC4yMiAyMC45Mkw4OC4yMiAyMC45MlE4OS4wOSAyMC45MiA4OS41MyAyMC41M1E4OS45NyAyMC4xNCA5MC4wOSAxOS4yMkw5MC4wOSAxOS4yMkw5MS41NyAxOS4yMlE5MS40NCAyMC41OSA5MC41NiAyMS4zNVE4OS42OCAyMi4xMiA4OC4yMiAyMi4xMkw4OC4yMiAyMi4xMlE4Ny4yMCAyMi4xMiA4Ni40MyAyMS42M1E4NS42NSAyMS4xNSA4NS4yMyAyMC4yNlE4NC44MSAxOS4zNyA4NC43OSAxOC4xOVpNOTcuNTYgMTQuNjZMOTQuOTIgMTQuNjZMOTQuOTIgMTMuNDdMMTAxLjY5IDEzLjQ3TDEwMS42OSAxNC42Nkw5OS4wMyAxNC42Nkw5OS4wMyAyMkw5Ny41NiAyMkw5Ny41NiAxNC42NlpNMTA3LjAxIDIyTDEwNS41NCAyMkwxMDUuNTQgMTMuNDdMMTA3LjAxIDEzLjQ3TDEwNy4wMSAyMlpNMTExLjU1IDE4LjAwTDExMS41NSAxOC4wMEwxMTEuNTUgMTcuNTJRMTExLjU1IDE2LjI4IDExMi4wMCAxNS4zMlExMTIuNDQgMTQuMzcgMTEzLjI0IDEzLjg2UTExNC4wNSAxMy4zNSAxMTUuMDkgMTMuMzVRMTE2LjE0IDEzLjM1IDExNi45NCAxMy44NVExMTcuNzUgMTQuMzUgMTE4LjE5IDE1LjI5UTExOC42MyAxNi4yMyAxMTguNjMgMTcuNDhMMTE4LjYzIDE3LjQ4TDExOC42MyAxNy45NlExMTguNjMgMTkuMjEgMTE4LjIwIDIwLjE2UTExNy43NiAyMS4xMCAxMTYuOTYgMjEuNjFRMTE2LjE1IDIyLjEyIDExNS4xMCAyMi4xMkwxMTUuMTAgMjIuMTJRMTE0LjA3IDIyLjEyIDExMy4yNiAyMS42MVExMTIuNDQgMjEuMTAgMTEyLjAwIDIwLjE3UTExMS41NiAxOS4yMyAxMTEuNTUgMTguMDBaTTExMy4wNCAxNy40NkwxMTMuMDQgMTcuOTZRMTEzLjA0IDE5LjM2IDExMy41OCAyMC4xM1ExMTQuMTMgMjAuOTAgMTE1LjEwIDIwLjkwTDExNS4xMCAyMC45MFExMTYuMDkgMjAuOTAgMTE2LjYyIDIwLjE1UTExNy4xNSAxOS40MCAxMTcuMTUgMTcuOTZMMTE3LjE1IDE3Ljk2TDExNy4xNSAxNy41MVExMTcuMTUgMTYuMDkgMTE2LjYxIDE1LjM0UTExNi4wOCAxNC41OCAxMTUuMDkgMTQuNThMMTE1LjA5IDE0LjU4UTExNC4xMyAxNC41OCAxMTMuNTkgMTUuMzNRMTEzLjA1IDE2LjA5IDExMy4wNCAxNy40NkwxMTMuMDQgMTcuNDZaTTEyNC41OCAyMkwxMjMuMTAgMjJMMTIzLjEwIDEzLjQ3TDEyNC41OCAxMy40N0wxMjguMzkgMTkuNTRMMTI4LjM5IDEzLjQ3TDEyOS44NiAxMy40N0wxMjkuODYgMjJMMTI4LjM4IDIyTDEyNC41OCAxNS45NUwxMjQuNTggMjJaIiBmaWxsPSIjMDAwMDAwIi8+PHBhdGggY2xhc3M9InN2Z19fdGV4dCIgZD0iIiBmaWxsPSIjMDAwMDAwIiB4PSIxNTQuNTUiLz48L3N2Zz4=)](https://novelmovementcph.streamlit.app/Introduction_%F0%9F%8F%A0)
[![forthebadge](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI5OC4zOSIgaGVpZ2h0PSIzNSIgdmlld0JveD0iMCAwIDk4LjM5IDM1Ij48cmVjdCBjbGFzcz0ic3ZnX19yZWN0IiB4PSIwIiB5PSIwIiB3aWR0aD0iOTguMzkiIGhlaWdodD0iMzUiIGZpbGw9IiNBMUExQTEiLz48cmVjdCBjbGFzcz0ic3ZnX19yZWN0IiB4PSI5OC4zOSIgeT0iMCIgd2lkdGg9IjAiIGhlaWdodD0iMzUiIGZpbGw9IiM2RkMyREUiLz48cGF0aCBjbGFzcz0ic3ZnX190ZXh0IiBkPSJNMTUuNjkgMjJMMTQuMjIgMjJMMTQuMjIgMTMuNDdMMTYuMTQgMTMuNDdMMTguNjAgMjAuMDFMMjEuMDYgMTMuNDdMMjIuOTcgMTMuNDdMMjIuOTcgMjJMMjEuNDkgMjJMMjEuNDkgMTkuMTlMMjEuNjQgMTUuNDNMMTkuMTIgMjJMMTguMDYgMjJMMTUuNTUgMTUuNDNMMTUuNjkgMTkuMTlMMTUuNjkgMjJaTTMzLjI5IDIyTDI3LjcxIDIyTDI3LjcxIDEzLjQ3TDMzLjI1IDEzLjQ3TDMzLjI1IDE0LjY2TDI5LjE5IDE0LjY2TDI5LjE5IDE3LjAyTDMyLjcwIDE3LjAyTDMyLjcwIDE4LjE5TDI5LjE5IDE4LjE5TDI5LjE5IDIwLjgyTDMzLjI5IDIwLjgyTDMzLjI5IDIyWk0zOS4xNyAxNC42NkwzNi41MyAxNC42NkwzNi41MyAxMy40N0w0My4zMCAxMy40N0w0My4zMCAxNC42Nkw0MC42NCAxNC42Nkw0MC42NCAyMkwzOS4xNyAyMkwzOS4xNyAxNC42NlpNNDguNTQgMjJMNDcuMDUgMjJMNDcuMDUgMTMuNDdMNDguNTQgMTMuNDdMNDguNTQgMTcuMDJMNTIuMzUgMTcuMDJMNTIuMzUgMTMuNDdMNTMuODMgMTMuNDdMNTMuODMgMjJMNTIuMzUgMjJMNTIuMzUgMTguMjFMNDguNTQgMTguMjFMNDguNTQgMjJaTTU4LjMwIDE4LjAwTDU4LjMwIDE4LjAwTDU4LjMwIDE3LjUyUTU4LjMwIDE2LjI4IDU4Ljc0IDE1LjMyUTU5LjE4IDE0LjM3IDU5Ljk5IDEzLjg2UTYwLjc5IDEzLjM1IDYxLjg0IDEzLjM1UTYyLjg4IDEzLjM1IDYzLjY4IDEzLjg1UTY0LjQ5IDE0LjM1IDY0LjkzIDE1LjI5UTY1LjM3IDE2LjIzIDY1LjM4IDE3LjQ4TDY1LjM4IDE3LjQ4TDY1LjM4IDE3Ljk2UTY1LjM4IDE5LjIxIDY0Ljk0IDIwLjE2UTY0LjUxIDIxLjEwIDYzLjcwIDIxLjYxUTYyLjkwIDIyLjEyIDYxLjg1IDIyLjEyTDYxLjg1IDIyLjEyUTYwLjgxIDIyLjEyIDYwLjAwIDIxLjYxUTU5LjE5IDIxLjEwIDU4Ljc1IDIwLjE3UTU4LjMwIDE5LjIzIDU4LjMwIDE4LjAwWk01OS43OCAxNy40Nkw1OS43OCAxNy45NlE1OS43OCAxOS4zNiA2MC4zMyAyMC4xM1E2MC44OCAyMC45MCA2MS44NSAyMC45MEw2MS44NSAyMC45MFE2Mi44MyAyMC45MCA2My4zNiAyMC4xNVE2My44OSAxOS40MCA2My44OSAxNy45Nkw2My44OSAxNy45Nkw2My44OSAxNy41MVE2My44OSAxNi4wOSA2My4zNiAxNS4zNFE2Mi44MiAxNC41OCA2MS44NCAxNC41OEw2MS44NCAxNC41OFE2MC44OCAxNC41OCA2MC4zMyAxNS4zM1E1OS43OSAxNi4wOSA1OS43OCAxNy40Nkw1OS43OCAxNy40NlpNNzIuMzAgMjJMNjkuODQgMjJMNjkuODQgMTMuNDdMNzIuMzYgMTMuNDdRNzMuNDkgMTMuNDcgNzQuMzcgMTMuOTdRNzUuMjQgMTQuNDggNzUuNzIgMTUuNDBRNzYuMjAgMTYuMzMgNzYuMjAgMTcuNTJMNzYuMjAgMTcuNTJMNzYuMjAgMTcuOTVRNzYuMjAgMTkuMTYgNzUuNzIgMjAuMDhRNzUuMjQgMjEuMDAgNzQuMzQgMjEuNTBRNzMuNDUgMjIgNzIuMzAgMjJMNzIuMzAgMjJaTTcxLjMyIDE0LjY2TDcxLjMyIDIwLjgyTDcyLjI5IDIwLjgyUTczLjQ2IDIwLjgyIDc0LjA4IDIwLjA5UTc0LjcwIDE5LjM2IDc0LjcyIDE3Ljk5TDc0LjcyIDE3Ljk5TDc0LjcyIDE3LjUyUTc0LjcyIDE2LjEzIDc0LjExIDE1LjQwUTczLjUxIDE0LjY2IDcyLjM2IDE0LjY2TDcyLjM2IDE0LjY2TDcxLjMyIDE0LjY2Wk04MC4yMyAxOS40Mkw4MC4yMyAxOS40Mkw4MS43MiAxOS40MlE4MS43MiAyMC4xNSA4Mi4yMCAyMC41NVE4Mi42OCAyMC45NSA4My41NyAyMC45NUw4My41NyAyMC45NVE4NC4zNSAyMC45NSA4NC43NCAyMC42M1E4NS4xMyAyMC4zMiA4NS4xMyAxOS44MEw4NS4xMyAxOS44MFE4NS4xMyAxOS4yNCA4NC43MyAxOC45NFE4NC4zNCAxOC42MyA4My4zMSAxOC4zMlE4Mi4yNyAxOC4wMSA4MS42NiAxNy42M0w4MS42NiAxNy42M1E4MC41MCAxNi45MCA4MC41MCAxNS43Mkw4MC41MCAxNS43MlE4MC41MCAxNC42OSA4MS4zNCAxNC4wMlE4Mi4xOCAxMy4zNSA4My41MiAxMy4zNUw4My41MiAxMy4zNVE4NC40MSAxMy4zNSA4NS4xMSAxMy42OFE4NS44MSAxNC4wMSA4Ni4yMSAxNC42MVE4Ni42MCAxNS4yMiA4Ni42MCAxNS45Nkw4Ni42MCAxNS45Nkw4NS4xMyAxNS45NlE4NS4xMyAxNS4yOSA4NC43MSAxNC45MVE4NC4yOSAxNC41NCA4My41MSAxNC41NEw4My41MSAxNC41NFE4Mi43OCAxNC41NCA4Mi4zOCAxNC44NVE4MS45OCAxNS4xNiA4MS45OCAxNS43MUw4MS45OCAxNS43MVE4MS45OCAxNi4xOCA4Mi40MSAxNi41MFE4Mi44NSAxNi44MSA4My44NCAxNy4xMFE4NC44NCAxNy40MCA4NS40NCAxNy43OFE4Ni4wNSAxOC4xNiA4Ni4zMyAxOC42NVE4Ni42MSAxOS4xMyA4Ni42MSAxOS43OUw4Ni42MSAxOS43OVE4Ni42MSAyMC44NiA4NS43OSAyMS40OVE4NC45NyAyMi4xMiA4My41NyAyMi4xMkw4My41NyAyMi4xMlE4Mi42NSAyMi4xMiA4MS44NyAyMS43N1E4MS4xMCAyMS40MyA4MC42NyAyMC44M1E4MC4yMyAyMC4yMiA4MC4yMyAxOS40MloiIGZpbGw9IiMwMDAwMDAiLz48cGF0aCBjbGFzcz0ic3ZnX190ZXh0IiBkPSIiIGZpbGw9IiMwMDAwMDAiIHg9IjExMS4zOSIvPjwvc3ZnPg==)](https://novelmovementcph.streamlit.app/Methods_%E2%9C%8F%EF%B8%8F_)
[![forthebadge](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMjUuNjMiIGhlaWdodD0iMzUiIHZpZXdCb3g9IjAgMCAxMjUuNjMgMzUiPjxyZWN0IGNsYXNzPSJzdmdfX3JlY3QiIHg9IjAiIHk9IjAiIHdpZHRoPSIxMjUuNjMiIGhlaWdodD0iMzUiIGZpbGw9IiNBMUExQTEiLz48cmVjdCBjbGFzcz0ic3ZnX19yZWN0IiB4PSIxMjUuNjMiIHk9IjAiIHdpZHRoPSIwIiBoZWlnaHQ9IjM1IiBmaWxsPSIjNkZDMkRFIi8+PHBhdGggY2xhc3M9InN2Z19fdGV4dCIgZD0iTTEzLjk1IDE4LjE5TDEzLjk1IDE4LjE5TDEzLjk1IDE3LjM5UTEzLjk1IDE2LjE5IDE0LjM4IDE1LjI3UTE0LjgwIDE0LjM1IDE1LjYwIDEzLjg1UTE2LjQwIDEzLjM1IDE3LjQ1IDEzLjM1TDE3LjQ1IDEzLjM1UTE4Ljg2IDEzLjM1IDE5LjczIDE0LjEyUTIwLjU5IDE0Ljg5IDIwLjczIDE2LjI5TDIwLjczIDE2LjI5TDE5LjI1IDE2LjI5UTE5LjE0IDE1LjM3IDE4LjcxIDE0Ljk2UTE4LjI4IDE0LjU1IDE3LjQ1IDE0LjU1TDE3LjQ1IDE0LjU1UTE2LjQ4IDE0LjU1IDE1Ljk3IDE1LjI2UTE1LjQ1IDE1Ljk2IDE1LjQ0IDE3LjMzTDE1LjQ0IDE3LjMzTDE1LjQ0IDE4LjA5UTE1LjQ0IDE5LjQ3IDE1LjkzIDIwLjIwUTE2LjQzIDIwLjkyIDE3LjM4IDIwLjkyTDE3LjM4IDIwLjkyUTE4LjI1IDIwLjkyIDE4LjY5IDIwLjUzUTE5LjEzIDIwLjE0IDE5LjI1IDE5LjIyTDE5LjI1IDE5LjIyTDIwLjczIDE5LjIyUTIwLjYwIDIwLjU5IDE5LjcyIDIxLjM1UTE4Ljg0IDIyLjEyIDE3LjM4IDIyLjEyTDE3LjM4IDIyLjEyUTE2LjM2IDIyLjEyIDE1LjU5IDIxLjYzUTE0LjgxIDIxLjE1IDE0LjM5IDIwLjI2UTEzLjk3IDE5LjM3IDEzLjk1IDE4LjE5Wk0yNC43NyAxOC4wMEwyNC43NyAxOC4wMEwyNC43NyAxNy41MlEyNC43NyAxNi4yOCAyNS4yMSAxNS4zMlEyNS42NSAxNC4zNyAyNi40NiAxMy44NlEyNy4yNyAxMy4zNSAyOC4zMSAxMy4zNVEyOS4zNSAxMy4zNSAzMC4xNiAxMy44NVEzMC45NiAxNC4zNSAzMS40MCAxNS4yOVEzMS44NCAxNi4yMyAzMS44NSAxNy40OEwzMS44NSAxNy40OEwzMS44NSAxNy45NlEzMS44NSAxOS4yMSAzMS40MSAyMC4xNlEzMC45OCAyMS4xMCAzMC4xOCAyMS42MVEyOS4zNyAyMi4xMiAyOC4zMiAyMi4xMkwyOC4zMiAyMi4xMlEyNy4yOCAyMi4xMiAyNi40NyAyMS42MVEyNS42NiAyMS4xMCAyNS4yMiAyMC4xN1EyNC43OCAxOS4yMyAyNC43NyAxOC4wMFpNMjYuMjUgMTcuNDZMMjYuMjUgMTcuOTZRMjYuMjUgMTkuMzYgMjYuODAgMjAuMTNRMjcuMzUgMjAuOTAgMjguMzIgMjAuOTBMMjguMzIgMjAuOTBRMjkuMzEgMjAuOTAgMjkuODQgMjAuMTVRMzAuMzcgMTkuNDAgMzAuMzcgMTcuOTZMMzAuMzcgMTcuOTZMMzAuMzcgMTcuNTFRMzAuMzcgMTYuMDkgMjkuODMgMTUuMzRRMjkuMjkgMTQuNTggMjguMzEgMTQuNThMMjguMzEgMTQuNThRMjcuMzUgMTQuNTggMjYuODEgMTUuMzNRMjYuMjYgMTYuMDkgMjYuMjUgMTcuNDZMMjYuMjUgMTcuNDZaTTM3LjgwIDIyTDM2LjMxIDIyTDM2LjMxIDEzLjQ3TDM3LjgwIDEzLjQ3TDQxLjYxIDE5LjU0TDQxLjYxIDEzLjQ3TDQzLjA4IDEzLjQ3TDQzLjA4IDIyTDQxLjYwIDIyTDM3LjgwIDE1Ljk1TDM3LjgwIDIyWk00Ny41NSAxOC4xOUw0Ny41NSAxOC4xOUw0Ny41NSAxNy4zOVE0Ny41NSAxNi4xOSA0Ny45OCAxNS4yN1E0OC40MSAxNC4zNSA0OS4yMSAxMy44NVE1MC4wMSAxMy4zNSA1MS4wNiAxMy4zNUw1MS4wNiAxMy4zNVE1Mi40NyAxMy4zNSA1My4zMyAxNC4xMlE1NC4xOSAxNC44OSA1NC4zMyAxNi4yOUw1NC4zMyAxNi4yOUw1Mi44NSAxNi4yOVE1Mi43NSAxNS4zNyA1Mi4zMiAxNC45NlE1MS44OSAxNC41NSA1MS4wNiAxNC41NUw1MS4wNiAxNC41NVE1MC4wOSAxNC41NSA0OS41NyAxNS4yNlE0OS4wNSAxNS45NiA0OS4wNCAxNy4zM0w0OS4wNCAxNy4zM0w0OS4wNCAxOC4wOVE0OS4wNCAxOS40NyA0OS41MyAyMC4yMFE1MC4wMyAyMC45MiA1MC45OCAyMC45Mkw1MC45OCAyMC45MlE1MS44NiAyMC45MiA1Mi4zMCAyMC41M1E1Mi43NCAyMC4xNCA1Mi44NSAxOS4yMkw1Mi44NSAxOS4yMkw1NC4zMyAxOS4yMlE1NC4yMCAyMC41OSA1My4zMiAyMS4zNVE1Mi40NCAyMi4xMiA1MC45OCAyMi4xMkw1MC45OCAyMi4xMlE0OS45NyAyMi4xMiA0OS4xOSAyMS42M1E0OC40MSAyMS4xNSA0Ny45OSAyMC4yNlE0Ny41NyAxOS4zNyA0Ny41NSAxOC4xOVpNNjQuMDAgMjJMNTguNjQgMjJMNTguNjQgMTMuNDdMNjAuMTMgMTMuNDdMNjAuMTMgMjAuODJMNjQuMDAgMjAuODJMNjQuMDAgMjJaTTY3Ljk5IDE5LjE2TDY3Ljk5IDE5LjE2TDY3Ljk5IDEzLjQ3TDY5LjQ3IDEzLjQ3TDY5LjQ3IDE5LjE4UTY5LjQ3IDIwLjAzIDY5LjkwIDIwLjQ4UTcwLjMzIDIwLjkzIDcxLjE4IDIwLjkzTDcxLjE4IDIwLjkzUTcyLjg5IDIwLjkzIDcyLjg5IDE5LjEzTDcyLjg5IDE5LjEzTDcyLjg5IDEzLjQ3TDc0LjM2IDEzLjQ3TDc0LjM2IDE5LjE3UTc0LjM2IDIwLjUzIDczLjQ5IDIxLjMyUTcyLjYyIDIyLjEyIDcxLjE4IDIyLjEyTDcxLjE4IDIyLjEyUTY5LjcxIDIyLjEyIDY4Ljg1IDIxLjMzUTY3Ljk5IDIwLjU1IDY3Ljk5IDE5LjE2Wk03OC41MCAxOS40Mkw3OC41MCAxOS40Mkw3OS45OCAxOS40MlE3OS45OCAyMC4xNSA4MC40NiAyMC41NVE4MC45NCAyMC45NSA4MS44NCAyMC45NUw4MS44NCAyMC45NVE4Mi42MSAyMC45NSA4My4wMCAyMC42M1E4My4zOSAyMC4zMiA4My4zOSAxOS44MEw4My4zOSAxOS44MFE4My4zOSAxOS4yNCA4My4wMCAxOC45NFE4Mi42MCAxOC42MyA4MS41NyAxOC4zMlE4MC41NCAxOC4wMSA3OS45MyAxNy42M0w3OS45MyAxNy42M1E3OC43NiAxNi45MCA3OC43NiAxNS43Mkw3OC43NiAxNS43MlE3OC43NiAxNC42OSA3OS42MCAxNC4wMlE4MC40NSAxMy4zNSA4MS43OSAxMy4zNUw4MS43OSAxMy4zNVE4Mi42OCAxMy4zNSA4My4zOCAxMy42OFE4NC4wNyAxNC4wMSA4NC40NyAxNC42MVE4NC44NyAxNS4yMiA4NC44NyAxNS45Nkw4NC44NyAxNS45Nkw4My4zOSAxNS45NlE4My4zOSAxNS4yOSA4Mi45NyAxNC45MVE4Mi41NiAxNC41NCA4MS43OCAxNC41NEw4MS43OCAxNC41NFE4MS4wNSAxNC41NCA4MC42NSAxNC44NVE4MC4yNSAxNS4xNiA4MC4yNSAxNS43MUw4MC4yNSAxNS43MVE4MC4yNSAxNi4xOCA4MC42OCAxNi41MFE4MS4xMSAxNi44MSA4Mi4xMSAxNy4xMFE4My4xMSAxNy40MCA4My43MSAxNy43OFE4NC4zMSAxOC4xNiA4NC41OSAxOC42NVE4NC44OCAxOS4xMyA4NC44OCAxOS43OUw4NC44OCAxOS43OVE4NC44OCAyMC44NiA4NC4wNiAyMS40OVE4My4yNCAyMi4xMiA4MS44NCAyMi4xMkw4MS44NCAyMi4xMlE4MC45MSAyMi4xMiA4MC4xNCAyMS43N1E3OS4zNiAyMS40MyA3OC45MyAyMC44M1E3OC41MCAyMC4yMiA3OC41MCAxOS40MlpNOTAuNzMgMjJMODkuMjUgMjJMODkuMjUgMTMuNDdMOTAuNzMgMTMuNDdMOTAuNzMgMjJaTTk1LjI3IDE4LjAwTDk1LjI3IDE4LjAwTDk1LjI3IDE3LjUyUTk1LjI3IDE2LjI4IDk1LjcxIDE1LjMyUTk2LjE1IDE0LjM3IDk2Ljk2IDEzLjg2UTk3Ljc3IDEzLjM1IDk4LjgxIDEzLjM1UTk5Ljg1IDEzLjM1IDEwMC42NiAxMy44NVExMDEuNDYgMTQuMzUgMTAxLjkwIDE1LjI5UTEwMi4zNCAxNi4yMyAxMDIuMzUgMTcuNDhMMTAyLjM1IDE3LjQ4TDEwMi4zNSAxNy45NlExMDIuMzUgMTkuMjEgMTAxLjkxIDIwLjE2UTEwMS40OCAyMS4xMCAxMDAuNjggMjEuNjFROTkuODcgMjIuMTIgOTguODIgMjIuMTJMOTguODIgMjIuMTJROTcuNzggMjIuMTIgOTYuOTcgMjEuNjFROTYuMTYgMjEuMTAgOTUuNzIgMjAuMTdROTUuMjggMTkuMjMgOTUuMjcgMTguMDBaTTk2Ljc1IDE3LjQ2TDk2Ljc1IDE3Ljk2UTk2Ljc1IDE5LjM2IDk3LjMwIDIwLjEzUTk3Ljg1IDIwLjkwIDk4LjgyIDIwLjkwTDk4LjgyIDIwLjkwUTk5LjgxIDIwLjkwIDEwMC4zNCAyMC4xNVExMDAuODcgMTkuNDAgMTAwLjg3IDE3Ljk2TDEwMC44NyAxNy45NkwxMDAuODcgMTcuNTFRMTAwLjg3IDE2LjA5IDEwMC4zMyAxNS4zNFE5OS43OSAxNC41OCA5OC44MSAxNC41OEw5OC44MSAxNC41OFE5Ny44NSAxNC41OCA5Ny4zMSAxNS4zM1E5Ni43NiAxNi4wOSA5Ni43NSAxNy40Nkw5Ni43NSAxNy40NlpNMTA4LjMwIDIyTDEwNi44MSAyMkwxMDYuODEgMTMuNDdMMTA4LjMwIDEzLjQ3TDExMi4xMSAxOS41NEwxMTIuMTEgMTMuNDdMMTEzLjU4IDEzLjQ3TDExMy41OCAyMkwxMTIuMTAgMjJMMTA4LjMwIDE1Ljk1TDEwOC4zMCAyMloiIGZpbGw9IiMwMDAwMDAiLz48cGF0aCBjbGFzcz0ic3ZnX190ZXh0IiBkPSIiIGZpbGw9IiMwMDAwMDAiIHg9IjEzOC42MyIvPjwvc3ZnPg==)](https://novelmovementcph.streamlit.app/Conclusion_%F0%9F%92%8A)
"""
st.title("Results")
c1, c2 = st.columns([3,1])
participantsfeatures = c1.selectbox("Novelty Detected Movement", ["Regression", "Participants", "Features"])
allptdata = pd.read_pickle("https://raw.githubusercontent.com/chags1313/cphresearchday/main/pages/alld.pkl")
comb = pd.read_csv("https://raw.githubusercontent.com/chags1313/cphresearchday/main/pages/comb.csv")
if participantsfeatures == 'Regression':
    hs = c2.radio("hs", ['Hand', 'Arm'], horizontal = True, label_visibility='hidden')
    if hs == 'Hand':
        v = 'Hand'
        text = "R^2 = 0.84, P-Value = <0.01"
    if hs == 'Arm':
        v = 'Side'
        text = "R^2 = 0.07, P-Value = 0.48"
    fig = px.scatter(comb[comb['Class']==v], x= 'Novelty Score', y = 'CUET Score', trendline = 'ols', trendline_color_override='black')
    fig.update_layout(showlegend=False, font_size = 28)
    fig.update_traces(marker={'size': 24})
    fig.update_layout(paper_bgcolor=None, plot_bgcolor=None, title = text)
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=-0.15,
        xanchor="right",
        x=0.8
    ))
    fig.update_xaxes(title = "Post-Test Novel UE Movement Scores")
    fig.update_yaxes(title = "CUE-T Post-Test Overall Score")
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar':False})
    with st.expander("Explanation"):
        """
        The chart above depicts the relationship between novelty detected upper extremity movement scores and clincally assessed upper extremity function scores from the capabilities of upper extremity test.
        """
if participantsfeatures == 'Participants':
    pt = c2.selectbox("Select Example Participant", options = allptdata['PT'].unique())
    figdata = allptdata[allptdata['cuet']=='Cuet2']
    figdata = figdata[figdata['PT'] == pt]
    figdata['s'] = figdata.index
    figdata["Series"] = figdata.groupby("PT")['s'].apply(lambda x: x.groupby(x).ngroup() + 1)
    figdata['Cue-T'] = figdata['CUET All Score']
    figdata['Novel Movement'] = figdata['Novel Movement'].replace([0,1], ['Baseline Related Movement', 'Novel UE Movement'])
    fig = px.scatter(figdata, x='Series', y = 'Resultant (m/s^2)_mean', 
                color = 'Novel Movement',
                color_discrete_map={'Non-Novel UE Movement': 'red', 'Novel UE Movement': 'lightsteelblue'}, 
                category_orders={'Novel Movement': ['Non-Novel UE Movement', 'Novel UE Movement']}, 
                hover_data = ['class'])
    fig.update_layout(height=450, width=1300, showlegend=True, font_size = 28)
    fig.update_layout(paper_bgcolor=None, plot_bgcolor=None)

    #fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
    fig.update_traces(marker={'size': 5})
    fig.update_xaxes(showgrid=False, zeroline=True, title = "Time", showticklabels=False)
    fig.update_yaxes(showgrid=True, zeroline=True, title = 'Acceleration (sqrt(x + y + z) M/S^2)')
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=-0.1,
        xanchor="right",
        x=0.5
    ))

    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar':False})
    with st.expander("Explanation"):
        """
        The plot above showcases the acceleration over time during the post-test CUE-T. The blue dots indicate the points in time when novel UE movements were detected with the LOF algorithm. The red dots indicate the points in time when baseline-related movement were detected. The LOF model was trained on baseline data from the CUE-T sensor-based movement and applied to all accerlation features. The acceleration values shown here are an example summary of movement. 
        """
if participantsfeatures == 'Features':
    handarm = c2.radio("Hand or Side", options = ["Hand", "Arm"], horizontal = True, label_visibility = 'hidden')
    if handarm == "Hand":
        d = allptdata[allptdata['class'] == 'hand']
    if handarm == "Arm":
        d = allptdata[allptdata['class'] == 'side']
    def pc(data):
        fig = go.Figure(data=
            go.Parcoords(
                line = dict(color = data['Novelty Score'],
                        colorscale = 'rdbu', cmin = 1, cmid = 3, cmax = 4), 
                dimensions = list([
                    dict(range = [data['Resultant (m/s^2)_mean'].min(),data['Resultant (m/s^2)_mean'].max()],
                        label = 'Mean', values = data['Resultant (m/s^2)_mean']),
                    dict(range = [data['Resultant (m/s^2)_min'].min(),data['Resultant (m/s^2)_min'].max()],
                        label = 'Min', values = data['Resultant (m/s^2)_min']),
                    dict(range = [data['Resultant (m/s^2)_max'].min(),data['Resultant (m/s^2)_max'].max()],
                        label = 'Max', values = data['Resultant (m/s^2)_max']),
                    dict(range = [data['Resultant (m/s^2)_std'].min(),data['Resultant (m/s^2)_std'].max()],
                        label = 'Std', values = data['Resultant (m/s^2)_std']),
                    dict(range = [data['Resultant (m/s^2)_energy'].min(),data['Resultant (m/s^2)_energy'].max()],
                        label = 'Energy', values = data['Resultant (m/s^2)_energy']),
                    dict(range = [data['Novelty Score'].min(),data['Novelty Score'].max()],
                        label = 'Novelty Score', values = data['Novelty Score'])
                ])
            )
        )

        fig.update_layout(paper_bgcolor=None, plot_bgcolor=None)
        with st.expander("Explanation"):
            """
            This parallel coordinates plot provides a way to look across multiple acceleration features and assess relationships with novel UE movement scores. Each acceleration feature is represented by a separate x-axis. All the axes are equally spaced and parallel to each other. Each axis has a different scale and unit of measurement that showcases the minimum value of each feature on the bottom and maxiumum value on the top of the y-axis. Each upper extremity movement observed across participants is plotted as a single line and is colored to represent the novel UE movement score, ranging from 1 (baseline-related movement) in red to 4 (novel UE movement) in blue.

            """

        return fig
    st.plotly_chart(pc(d), use_container_width=True, config={'displayModeBar':False})
 
spacer1, spacer2, spacer3 = st.columns(3)
spacer2.markdown(
"""
[![forthebadge](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNTcuNTQiIGhlaWdodD0iMzUiIHZpZXdCb3g9IjAgMCAxNTcuNTQgMzUiPjxyZWN0IGNsYXNzPSJzdmdfX3JlY3QiIHg9IjAiIHk9IjAiIHdpZHRoPSIxMjcuNjMiIGhlaWdodD0iMzUiIGZpbGw9IiMwMDAwMDAiLz48cmVjdCBjbGFzcz0ic3ZnX19yZWN0IiB4PSIxMjUuNjMiIHk9IjAiIHdpZHRoPSIzMS45MDk5OTk5OTk5OTk5OTciIGhlaWdodD0iMzUiIGZpbGw9IiMzQzlBRDUiLz48cGF0aCBjbGFzcz0ic3ZnX190ZXh0IiBkPSJNMTMuOTUgMTguMTlMMTMuOTUgMTguMTlMMTMuOTUgMTcuMzlRMTMuOTUgMTYuMTkgMTQuMzggMTUuMjdRMTQuODAgMTQuMzUgMTUuNjAgMTMuODVRMTYuNDAgMTMuMzUgMTcuNDUgMTMuMzVMMTcuNDUgMTMuMzVRMTguODYgMTMuMzUgMTkuNzMgMTQuMTJRMjAuNTkgMTQuODkgMjAuNzMgMTYuMjlMMjAuNzMgMTYuMjlMMTkuMjUgMTYuMjlRMTkuMTQgMTUuMzcgMTguNzEgMTQuOTZRMTguMjggMTQuNTUgMTcuNDUgMTQuNTVMMTcuNDUgMTQuNTVRMTYuNDggMTQuNTUgMTUuOTcgMTUuMjZRMTUuNDUgMTUuOTYgMTUuNDQgMTcuMzNMMTUuNDQgMTcuMzNMMTUuNDQgMTguMDlRMTUuNDQgMTkuNDcgMTUuOTMgMjAuMjBRMTYuNDMgMjAuOTIgMTcuMzggMjAuOTJMMTcuMzggMjAuOTJRMTguMjUgMjAuOTIgMTguNjkgMjAuNTNRMTkuMTMgMjAuMTQgMTkuMjUgMTkuMjJMMTkuMjUgMTkuMjJMMjAuNzMgMTkuMjJRMjAuNjAgMjAuNTkgMTkuNzIgMjEuMzVRMTguODQgMjIuMTIgMTcuMzggMjIuMTJMMTcuMzggMjIuMTJRMTYuMzYgMjIuMTIgMTUuNTkgMjEuNjNRMTQuODEgMjEuMTUgMTQuMzkgMjAuMjZRMTMuOTcgMTkuMzcgMTMuOTUgMTguMTlaTTI0Ljc3IDE4LjAwTDI0Ljc3IDE4LjAwTDI0Ljc3IDE3LjUyUTI0Ljc3IDE2LjI4IDI1LjIxIDE1LjMyUTI1LjY1IDE0LjM3IDI2LjQ2IDEzLjg2UTI3LjI3IDEzLjM1IDI4LjMxIDEzLjM1UTI5LjM1IDEzLjM1IDMwLjE2IDEzLjg1UTMwLjk2IDE0LjM1IDMxLjQwIDE1LjI5UTMxLjg0IDE2LjIzIDMxLjg1IDE3LjQ4TDMxLjg1IDE3LjQ4TDMxLjg1IDE3Ljk2UTMxLjg1IDE5LjIxIDMxLjQxIDIwLjE2UTMwLjk4IDIxLjEwIDMwLjE4IDIxLjYxUTI5LjM3IDIyLjEyIDI4LjMyIDIyLjEyTDI4LjMyIDIyLjEyUTI3LjI4IDIyLjEyIDI2LjQ3IDIxLjYxUTI1LjY2IDIxLjEwIDI1LjIyIDIwLjE3UTI0Ljc4IDE5LjIzIDI0Ljc3IDE4LjAwWk0yNi4yNSAxNy40NkwyNi4yNSAxNy45NlEyNi4yNSAxOS4zNiAyNi44MCAyMC4xM1EyNy4zNSAyMC45MCAyOC4zMiAyMC45MEwyOC4zMiAyMC45MFEyOS4zMSAyMC45MCAyOS44NCAyMC4xNVEzMC4zNyAxOS40MCAzMC4zNyAxNy45NkwzMC4zNyAxNy45NkwzMC4zNyAxNy41MVEzMC4zNyAxNi4wOSAyOS44MyAxNS4zNFEyOS4yOSAxNC41OCAyOC4zMSAxNC41OEwyOC4zMSAxNC41OFEyNy4zNSAxNC41OCAyNi44MSAxNS4zM1EyNi4yNiAxNi4wOSAyNi4yNSAxNy40NkwyNi4yNSAxNy40NlpNMzcuODAgMjJMMzYuMzEgMjJMMzYuMzEgMTMuNDdMMzcuODAgMTMuNDdMNDEuNjEgMTkuNTRMNDEuNjEgMTMuNDdMNDMuMDggMTMuNDdMNDMuMDggMjJMNDEuNjAgMjJMMzcuODAgMTUuOTVMMzcuODAgMjJaTTQ3LjU1IDE4LjE5TDQ3LjU1IDE4LjE5TDQ3LjU1IDE3LjM5UTQ3LjU1IDE2LjE5IDQ3Ljk4IDE1LjI3UTQ4LjQxIDE0LjM1IDQ5LjIxIDEzLjg1UTUwLjAxIDEzLjM1IDUxLjA2IDEzLjM1TDUxLjA2IDEzLjM1UTUyLjQ3IDEzLjM1IDUzLjMzIDE0LjEyUTU0LjE5IDE0Ljg5IDU0LjMzIDE2LjI5TDU0LjMzIDE2LjI5TDUyLjg1IDE2LjI5UTUyLjc1IDE1LjM3IDUyLjMyIDE0Ljk2UTUxLjg5IDE0LjU1IDUxLjA2IDE0LjU1TDUxLjA2IDE0LjU1UTUwLjA5IDE0LjU1IDQ5LjU3IDE1LjI2UTQ5LjA1IDE1Ljk2IDQ5LjA0IDE3LjMzTDQ5LjA0IDE3LjMzTDQ5LjA0IDE4LjA5UTQ5LjA0IDE5LjQ3IDQ5LjUzIDIwLjIwUTUwLjAzIDIwLjkyIDUwLjk4IDIwLjkyTDUwLjk4IDIwLjkyUTUxLjg2IDIwLjkyIDUyLjMwIDIwLjUzUTUyLjc0IDIwLjE0IDUyLjg1IDE5LjIyTDUyLjg1IDE5LjIyTDU0LjMzIDE5LjIyUTU0LjIwIDIwLjU5IDUzLjMyIDIxLjM1UTUyLjQ0IDIyLjEyIDUwLjk4IDIyLjEyTDUwLjk4IDIyLjEyUTQ5Ljk3IDIyLjEyIDQ5LjE5IDIxLjYzUTQ4LjQxIDIxLjE1IDQ3Ljk5IDIwLjI2UTQ3LjU3IDE5LjM3IDQ3LjU1IDE4LjE5Wk02NC4wMCAyMkw1OC42NCAyMkw1OC42NCAxMy40N0w2MC4xMyAxMy40N0w2MC4xMyAyMC44Mkw2NC4wMCAyMC44Mkw2NC4wMCAyMlpNNjcuOTkgMTkuMTZMNjcuOTkgMTkuMTZMNjcuOTkgMTMuNDdMNjkuNDcgMTMuNDdMNjkuNDcgMTkuMThRNjkuNDcgMjAuMDMgNjkuOTAgMjAuNDhRNzAuMzMgMjAuOTMgNzEuMTggMjAuOTNMNzEuMTggMjAuOTNRNzIuODkgMjAuOTMgNzIuODkgMTkuMTNMNzIuODkgMTkuMTNMNzIuODkgMTMuNDdMNzQuMzYgMTMuNDdMNzQuMzYgMTkuMTdRNzQuMzYgMjAuNTMgNzMuNDkgMjEuMzJRNzIuNjIgMjIuMTIgNzEuMTggMjIuMTJMNzEuMTggMjIuMTJRNjkuNzEgMjIuMTIgNjguODUgMjEuMzNRNjcuOTkgMjAuNTUgNjcuOTkgMTkuMTZaTTc4LjUwIDE5LjQyTDc4LjUwIDE5LjQyTDc5Ljk4IDE5LjQyUTc5Ljk4IDIwLjE1IDgwLjQ2IDIwLjU1UTgwLjk0IDIwLjk1IDgxLjg0IDIwLjk1TDgxLjg0IDIwLjk1UTgyLjYxIDIwLjk1IDgzLjAwIDIwLjYzUTgzLjM5IDIwLjMyIDgzLjM5IDE5LjgwTDgzLjM5IDE5LjgwUTgzLjM5IDE5LjI0IDgzLjAwIDE4Ljk0UTgyLjYwIDE4LjYzIDgxLjU3IDE4LjMyUTgwLjU0IDE4LjAxIDc5LjkzIDE3LjYzTDc5LjkzIDE3LjYzUTc4Ljc2IDE2LjkwIDc4Ljc2IDE1LjcyTDc4Ljc2IDE1LjcyUTc4Ljc2IDE0LjY5IDc5LjYwIDE0LjAyUTgwLjQ1IDEzLjM1IDgxLjc5IDEzLjM1TDgxLjc5IDEzLjM1UTgyLjY4IDEzLjM1IDgzLjM4IDEzLjY4UTg0LjA3IDE0LjAxIDg0LjQ3IDE0LjYxUTg0Ljg3IDE1LjIyIDg0Ljg3IDE1Ljk2TDg0Ljg3IDE1Ljk2TDgzLjM5IDE1Ljk2UTgzLjM5IDE1LjI5IDgyLjk3IDE0LjkxUTgyLjU2IDE0LjU0IDgxLjc4IDE0LjU0TDgxLjc4IDE0LjU0UTgxLjA1IDE0LjU0IDgwLjY1IDE0Ljg1UTgwLjI1IDE1LjE2IDgwLjI1IDE1LjcxTDgwLjI1IDE1LjcxUTgwLjI1IDE2LjE4IDgwLjY4IDE2LjUwUTgxLjExIDE2LjgxIDgyLjExIDE3LjEwUTgzLjExIDE3LjQwIDgzLjcxIDE3Ljc4UTg0LjMxIDE4LjE2IDg0LjU5IDE4LjY1UTg0Ljg4IDE5LjEzIDg0Ljg4IDE5Ljc5TDg0Ljg4IDE5Ljc5UTg0Ljg4IDIwLjg2IDg0LjA2IDIxLjQ5UTgzLjI0IDIyLjEyIDgxLjg0IDIyLjEyTDgxLjg0IDIyLjEyUTgwLjkxIDIyLjEyIDgwLjE0IDIxLjc3UTc5LjM2IDIxLjQzIDc4LjkzIDIwLjgzUTc4LjUwIDIwLjIyIDc4LjUwIDE5LjQyWk05MC43MyAyMkw4OS4yNSAyMkw4OS4yNSAxMy40N0w5MC43MyAxMy40N0w5MC43MyAyMlpNOTUuMjcgMTguMDBMOTUuMjcgMTguMDBMOTUuMjcgMTcuNTJROTUuMjcgMTYuMjggOTUuNzEgMTUuMzJROTYuMTUgMTQuMzcgOTYuOTYgMTMuODZROTcuNzcgMTMuMzUgOTguODEgMTMuMzVROTkuODUgMTMuMzUgMTAwLjY2IDEzLjg1UTEwMS40NiAxNC4zNSAxMDEuOTAgMTUuMjlRMTAyLjM0IDE2LjIzIDEwMi4zNSAxNy40OEwxMDIuMzUgMTcuNDhMMTAyLjM1IDE3Ljk2UTEwMi4zNSAxOS4yMSAxMDEuOTEgMjAuMTZRMTAxLjQ4IDIxLjEwIDEwMC42OCAyMS42MVE5OS44NyAyMi4xMiA5OC44MiAyMi4xMkw5OC44MiAyMi4xMlE5Ny43OCAyMi4xMiA5Ni45NyAyMS42MVE5Ni4xNiAyMS4xMCA5NS43MiAyMC4xN1E5NS4yOCAxOS4yMyA5NS4yNyAxOC4wMFpNOTYuNzUgMTcuNDZMOTYuNzUgMTcuOTZROTYuNzUgMTkuMzYgOTcuMzAgMjAuMTNROTcuODUgMjAuOTAgOTguODIgMjAuOTBMOTguODIgMjAuOTBROTkuODEgMjAuOTAgMTAwLjM0IDIwLjE1UTEwMC44NyAxOS40MCAxMDAuODcgMTcuOTZMMTAwLjg3IDE3Ljk2TDEwMC44NyAxNy41MVExMDAuODcgMTYuMDkgMTAwLjMzIDE1LjM0UTk5Ljc5IDE0LjU4IDk4LjgxIDE0LjU4TDk4LjgxIDE0LjU4UTk3Ljg1IDE0LjU4IDk3LjMxIDE1LjMzUTk2Ljc2IDE2LjA5IDk2Ljc1IDE3LjQ2TDk2Ljc1IDE3LjQ2Wk0xMDguMzAgMjJMMTA2LjgxIDIyTDEwNi44MSAxMy40N0wxMDguMzAgMTMuNDdMMTEyLjExIDE5LjU0TDExMi4xMSAxMy40N0wxMTMuNTggMTMuNDdMMTEzLjU4IDIyTDExMi4xMCAyMkwxMDguMzAgMTUuOTVMMTA4LjMwIDIyWiIgZmlsbD0iI0ZGRkZGRiIvPjxwYXRoIGNsYXNzPSJzdmdfX3RleHQiIGQ9Ik0xNDUuNTkgMTguNzJMMTM5LjY4IDIwLjkxTDEzOS42OCAxOS4xNkwxNDMuNTAgMTcuODBMMTM5LjY4IDE2LjQ1TDEzOS42OCAxNC42OUwxNDUuNTkgMTYuODhMMTQ1LjU5IDE4LjcyWiIgZmlsbD0iIzAwMDAwMCIgeD0iMTM4LjYzIi8+PC9zdmc+)](https://novelmovementcph.streamlit.app/Conclusion_%F0%9F%92%8A)
""")
