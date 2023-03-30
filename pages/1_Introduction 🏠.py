import streamlit as st
from PIL import Image
"""
[![forthebadge](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI5OC4zOSIgaGVpZ2h0PSIzNSIgdmlld0JveD0iMCAwIDk4LjM5IDM1Ij48cmVjdCBjbGFzcz0ic3ZnX19yZWN0IiB4PSIwIiB5PSIwIiB3aWR0aD0iOTguMzkiIGhlaWdodD0iMzUiIGZpbGw9IiNBMUExQTEiLz48cmVjdCBjbGFzcz0ic3ZnX19yZWN0IiB4PSI5OC4zOSIgeT0iMCIgd2lkdGg9IjAiIGhlaWdodD0iMzUiIGZpbGw9IiM2RkMyREUiLz48cGF0aCBjbGFzcz0ic3ZnX190ZXh0IiBkPSJNMTUuNjkgMjJMMTQuMjIgMjJMMTQuMjIgMTMuNDdMMTYuMTQgMTMuNDdMMTguNjAgMjAuMDFMMjEuMDYgMTMuNDdMMjIuOTcgMTMuNDdMMjIuOTcgMjJMMjEuNDkgMjJMMjEuNDkgMTkuMTlMMjEuNjQgMTUuNDNMMTkuMTIgMjJMMTguMDYgMjJMMTUuNTUgMTUuNDNMMTUuNjkgMTkuMTlMMTUuNjkgMjJaTTMzLjI5IDIyTDI3LjcxIDIyTDI3LjcxIDEzLjQ3TDMzLjI1IDEzLjQ3TDMzLjI1IDE0LjY2TDI5LjE5IDE0LjY2TDI5LjE5IDE3LjAyTDMyLjcwIDE3LjAyTDMyLjcwIDE4LjE5TDI5LjE5IDE4LjE5TDI5LjE5IDIwLjgyTDMzLjI5IDIwLjgyTDMzLjI5IDIyWk0zOS4xNyAxNC42NkwzNi41MyAxNC42NkwzNi41MyAxMy40N0w0My4zMCAxMy40N0w0My4zMCAxNC42Nkw0MC42NCAxNC42Nkw0MC42NCAyMkwzOS4xNyAyMkwzOS4xNyAxNC42NlpNNDguNTQgMjJMNDcuMDUgMjJMNDcuMDUgMTMuNDdMNDguNTQgMTMuNDdMNDguNTQgMTcuMDJMNTIuMzUgMTcuMDJMNTIuMzUgMTMuNDdMNTMuODMgMTMuNDdMNTMuODMgMjJMNTIuMzUgMjJMNTIuMzUgMTguMjFMNDguNTQgMTguMjFMNDguNTQgMjJaTTU4LjMwIDE4LjAwTDU4LjMwIDE4LjAwTDU4LjMwIDE3LjUyUTU4LjMwIDE2LjI4IDU4Ljc0IDE1LjMyUTU5LjE4IDE0LjM3IDU5Ljk5IDEzLjg2UTYwLjc5IDEzLjM1IDYxLjg0IDEzLjM1UTYyLjg4IDEzLjM1IDYzLjY4IDEzLjg1UTY0LjQ5IDE0LjM1IDY0LjkzIDE1LjI5UTY1LjM3IDE2LjIzIDY1LjM4IDE3LjQ4TDY1LjM4IDE3LjQ4TDY1LjM4IDE3Ljk2UTY1LjM4IDE5LjIxIDY0Ljk0IDIwLjE2UTY0LjUxIDIxLjEwIDYzLjcwIDIxLjYxUTYyLjkwIDIyLjEyIDYxLjg1IDIyLjEyTDYxLjg1IDIyLjEyUTYwLjgxIDIyLjEyIDYwLjAwIDIxLjYxUTU5LjE5IDIxLjEwIDU4Ljc1IDIwLjE3UTU4LjMwIDE5LjIzIDU4LjMwIDE4LjAwWk01OS43OCAxNy40Nkw1OS43OCAxNy45NlE1OS43OCAxOS4zNiA2MC4zMyAyMC4xM1E2MC44OCAyMC45MCA2MS44NSAyMC45MEw2MS44NSAyMC45MFE2Mi44MyAyMC45MCA2My4zNiAyMC4xNVE2My44OSAxOS40MCA2My44OSAxNy45Nkw2My44OSAxNy45Nkw2My44OSAxNy41MVE2My44OSAxNi4wOSA2My4zNiAxNS4zNFE2Mi44MiAxNC41OCA2MS44NCAxNC41OEw2MS44NCAxNC41OFE2MC44OCAxNC41OCA2MC4zMyAxNS4zM1E1OS43OSAxNi4wOSA1OS43OCAxNy40Nkw1OS43OCAxNy40NlpNNzIuMzAgMjJMNjkuODQgMjJMNjkuODQgMTMuNDdMNzIuMzYgMTMuNDdRNzMuNDkgMTMuNDcgNzQuMzcgMTMuOTdRNzUuMjQgMTQuNDggNzUuNzIgMTUuNDBRNzYuMjAgMTYuMzMgNzYuMjAgMTcuNTJMNzYuMjAgMTcuNTJMNzYuMjAgMTcuOTVRNzYuMjAgMTkuMTYgNzUuNzIgMjAuMDhRNzUuMjQgMjEuMDAgNzQuMzQgMjEuNTBRNzMuNDUgMjIgNzIuMzAgMjJMNzIuMzAgMjJaTTcxLjMyIDE0LjY2TDcxLjMyIDIwLjgyTDcyLjI5IDIwLjgyUTczLjQ2IDIwLjgyIDc0LjA4IDIwLjA5UTc0LjcwIDE5LjM2IDc0LjcyIDE3Ljk5TDc0LjcyIDE3Ljk5TDc0LjcyIDE3LjUyUTc0LjcyIDE2LjEzIDc0LjExIDE1LjQwUTczLjUxIDE0LjY2IDcyLjM2IDE0LjY2TDcyLjM2IDE0LjY2TDcxLjMyIDE0LjY2Wk04MC4yMyAxOS40Mkw4MC4yMyAxOS40Mkw4MS43MiAxOS40MlE4MS43MiAyMC4xNSA4Mi4yMCAyMC41NVE4Mi42OCAyMC45NSA4My41NyAyMC45NUw4My41NyAyMC45NVE4NC4zNSAyMC45NSA4NC43NCAyMC42M1E4NS4xMyAyMC4zMiA4NS4xMyAxOS44MEw4NS4xMyAxOS44MFE4NS4xMyAxOS4yNCA4NC43MyAxOC45NFE4NC4zNCAxOC42MyA4My4zMSAxOC4zMlE4Mi4yNyAxOC4wMSA4MS42NiAxNy42M0w4MS42NiAxNy42M1E4MC41MCAxNi45MCA4MC41MCAxNS43Mkw4MC41MCAxNS43MlE4MC41MCAxNC42OSA4MS4zNCAxNC4wMlE4Mi4xOCAxMy4zNSA4My41MiAxMy4zNUw4My41MiAxMy4zNVE4NC40MSAxMy4zNSA4NS4xMSAxMy42OFE4NS44MSAxNC4wMSA4Ni4yMSAxNC42MVE4Ni42MCAxNS4yMiA4Ni42MCAxNS45Nkw4Ni42MCAxNS45Nkw4NS4xMyAxNS45NlE4NS4xMyAxNS4yOSA4NC43MSAxNC45MVE4NC4yOSAxNC41NCA4My41MSAxNC41NEw4My41MSAxNC41NFE4Mi43OCAxNC41NCA4Mi4zOCAxNC44NVE4MS45OCAxNS4xNiA4MS45OCAxNS43MUw4MS45OCAxNS43MVE4MS45OCAxNi4xOCA4Mi40MSAxNi41MFE4Mi44NSAxNi44MSA4My44NCAxNy4xMFE4NC44NCAxNy40MCA4NS40NCAxNy43OFE4Ni4wNSAxOC4xNiA4Ni4zMyAxOC42NVE4Ni42MSAxOS4xMyA4Ni42MSAxOS43OUw4Ni42MSAxOS43OVE4Ni42MSAyMC44NiA4NS43OSAyMS40OVE4NC45NyAyMi4xMiA4My41NyAyMi4xMkw4My41NyAyMi4xMlE4Mi42NSAyMi4xMiA4MS44NyAyMS43N1E4MS4xMCAyMS40MyA4MC42NyAyMC44M1E4MC4yMyAyMC4yMiA4MC4yMyAxOS40MloiIGZpbGw9IiMwMDAwMDAiLz48cGF0aCBjbGFzcz0ic3ZnX190ZXh0IiBkPSIiIGZpbGw9IiMwMDAwMDAiIHg9IjExMS4zOSIvPjwvc3ZnPg==)](https://novelmovementcph.streamlit.app/Methods_%E2%9C%8F%EF%B8%8F_)
[![forthebadge](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI5Mi4yOCIgaGVpZ2h0PSIzNSIgdmlld0JveD0iMCAwIDkyLjI4IDM1Ij48cmVjdCBjbGFzcz0ic3ZnX19yZWN0IiB4PSIwIiB5PSIwIiB3aWR0aD0iOTIuMjgiIGhlaWdodD0iMzUiIGZpbGw9IiNBMUExQTEiLz48cmVjdCBjbGFzcz0ic3ZnX19yZWN0IiB4PSI5Mi4yOCIgeT0iMCIgd2lkdGg9IjAiIGhlaWdodD0iMzUiIGZpbGw9IiM2RkMyREUiLz48cGF0aCBjbGFzcz0ic3ZnX190ZXh0IiBkPSJNMTUuNzAgMjJMMTQuMjIgMjJMMTQuMjIgMTMuNDdMMTcuMjIgMTMuNDdRMTguNjkgMTMuNDcgMTkuNTAgMTQuMTNRMjAuMzAgMTQuNzkgMjAuMzAgMTYuMDVMMjAuMzAgMTYuMDVRMjAuMzAgMTYuOTAgMTkuODkgMTcuNDhRMTkuNDcgMTguMDYgMTguNzMgMTguMzdMMTguNzMgMTguMzdMMjAuNjUgMjEuOTJMMjAuNjUgMjJMMTkuMDYgMjJMMTcuMzUgMTguNzFMMTUuNzAgMTguNzFMMTUuNzAgMjJaTTE1LjcwIDE0LjY2TDE1LjcwIDE3LjUyTDE3LjIyIDE3LjUyUTE3Ljk3IDE3LjUyIDE4LjM5IDE3LjE1UTE4LjgyIDE2Ljc3IDE4LjgyIDE2LjExTDE4LjgyIDE2LjExUTE4LjgyIDE1LjQzIDE4LjQzIDE1LjA1UTE4LjA0IDE0LjY4IDE3LjI2IDE0LjY2TDE3LjI2IDE0LjY2TDE1LjcwIDE0LjY2Wk0zMC4yNyAyMkwyNC42OSAyMkwyNC42OSAxMy40N0wzMC4yMyAxMy40N0wzMC4yMyAxNC42NkwyNi4xOCAxNC42NkwyNi4xOCAxNy4wMkwyOS42OCAxNy4wMkwyOS42OCAxOC4xOUwyNi4xOCAxOC4xOUwyNi4xOCAyMC44MkwzMC4yNyAyMC44MkwzMC4yNyAyMlpNMzQuMDMgMTkuNDJMMzQuMDMgMTkuNDJMMzUuNTIgMTkuNDJRMzUuNTIgMjAuMTUgMzYuMDAgMjAuNTVRMzYuNDggMjAuOTUgMzcuMzcgMjAuOTVMMzcuMzcgMjAuOTVRMzguMTUgMjAuOTUgMzguNTQgMjAuNjNRMzguOTMgMjAuMzIgMzguOTMgMTkuODBMMzguOTMgMTkuODBRMzguOTMgMTkuMjQgMzguNTMgMTguOTRRMzguMTQgMTguNjMgMzcuMTAgMTguMzJRMzYuMDcgMTguMDEgMzUuNDYgMTcuNjNMMzUuNDYgMTcuNjNRMzQuMzAgMTYuOTAgMzQuMzAgMTUuNzJMMzQuMzAgMTUuNzJRMzQuMzAgMTQuNjkgMzUuMTQgMTQuMDJRMzUuOTggMTMuMzUgMzcuMzIgMTMuMzVMMzcuMzIgMTMuMzVRMzguMjEgMTMuMzUgMzguOTEgMTMuNjhRMzkuNjEgMTQuMDEgNDAuMDAgMTQuNjFRNDAuNDAgMTUuMjIgNDAuNDAgMTUuOTZMNDAuNDAgMTUuOTZMMzguOTMgMTUuOTZRMzguOTMgMTUuMjkgMzguNTEgMTQuOTFRMzguMDkgMTQuNTQgMzcuMzEgMTQuNTRMMzcuMzEgMTQuNTRRMzYuNTggMTQuNTQgMzYuMTggMTQuODVRMzUuNzggMTUuMTYgMzUuNzggMTUuNzFMMzUuNzggMTUuNzFRMzUuNzggMTYuMTggMzYuMjEgMTYuNTBRMzYuNjUgMTYuODEgMzcuNjQgMTcuMTBRMzguNjQgMTcuNDAgMzkuMjQgMTcuNzhRMzkuODUgMTguMTYgNDAuMTMgMTguNjVRNDAuNDEgMTkuMTMgNDAuNDEgMTkuNzlMNDAuNDEgMTkuNzlRNDAuNDEgMjAuODYgMzkuNTkgMjEuNDlRMzguNzcgMjIuMTIgMzcuMzcgMjIuMTJMMzcuMzcgMjIuMTJRMzYuNDUgMjIuMTIgMzUuNjcgMjEuNzdRMzQuODkgMjEuNDMgMzQuNDYgMjAuODNRMzQuMDMgMjAuMjIgMzQuMDMgMTkuNDJaTTQ0LjU2IDE5LjE2TDQ0LjU2IDE5LjE2TDQ0LjU2IDEzLjQ3TDQ2LjA0IDEzLjQ3TDQ2LjA0IDE5LjE4UTQ2LjA0IDIwLjAzIDQ2LjQ3IDIwLjQ4UTQ2LjkxIDIwLjkzIDQ3Ljc1IDIwLjkzTDQ3Ljc1IDIwLjkzUTQ5LjQ2IDIwLjkzIDQ5LjQ2IDE5LjEzTDQ5LjQ2IDE5LjEzTDQ5LjQ2IDEzLjQ3TDUwLjk0IDEzLjQ3TDUwLjk0IDE5LjE3UTUwLjk0IDIwLjUzIDUwLjA3IDIxLjMyUTQ5LjIwIDIyLjEyIDQ3Ljc1IDIyLjEyTDQ3Ljc1IDIyLjEyUTQ2LjI5IDIyLjEyIDQ1LjQyIDIxLjMzUTQ0LjU2IDIwLjU1IDQ0LjU2IDE5LjE2Wk02MC44NiAyMkw1NS41MSAyMkw1NS41MSAxMy40N0w1Ni45OSAxMy40N0w1Ni45OSAyMC44Mkw2MC44NiAyMC44Mkw2MC44NiAyMlpNNjYuNjcgMTQuNjZMNjQuMDMgMTQuNjZMNjQuMDMgMTMuNDdMNzAuODAgMTMuNDdMNzAuODAgMTQuNjZMNjguMTQgMTQuNjZMNjguMTQgMjJMNjYuNjcgMjJMNjYuNjcgMTQuNjZaTTc0LjEyIDE5LjQyTDc0LjEyIDE5LjQyTDc1LjYxIDE5LjQyUTc1LjYxIDIwLjE1IDc2LjA5IDIwLjU1UTc2LjU3IDIwLjk1IDc3LjQ2IDIwLjk1TDc3LjQ2IDIwLjk1UTc4LjI0IDIwLjk1IDc4LjYzIDIwLjYzUTc5LjAyIDIwLjMyIDc5LjAyIDE5LjgwTDc5LjAyIDE5LjgwUTc5LjAyIDE5LjI0IDc4LjYyIDE4Ljk0UTc4LjIyIDE4LjYzIDc3LjE5IDE4LjMyUTc2LjE2IDE4LjAxIDc1LjU1IDE3LjYzTDc1LjU1IDE3LjYzUTc0LjM5IDE2LjkwIDc0LjM5IDE1LjcyTDc0LjM5IDE1LjcyUTc0LjM5IDE0LjY5IDc1LjIzIDE0LjAyUTc2LjA3IDEzLjM1IDc3LjQxIDEzLjM1TDc3LjQxIDEzLjM1UTc4LjMwIDEzLjM1IDc5LjAwIDEzLjY4UTc5LjcwIDE0LjAxIDgwLjA5IDE0LjYxUTgwLjQ5IDE1LjIyIDgwLjQ5IDE1Ljk2TDgwLjQ5IDE1Ljk2TDc5LjAyIDE1Ljk2UTc5LjAyIDE1LjI5IDc4LjYwIDE0LjkxUTc4LjE4IDE0LjU0IDc3LjQwIDE0LjU0TDc3LjQwIDE0LjU0UTc2LjY3IDE0LjU0IDc2LjI3IDE0Ljg1UTc1Ljg3IDE1LjE2IDc1Ljg3IDE1LjcxTDc1Ljg3IDE1LjcxUTc1Ljg3IDE2LjE4IDc2LjMwIDE2LjUwUTc2Ljc0IDE2LjgxIDc3LjczIDE3LjEwUTc4LjczIDE3LjQwIDc5LjMzIDE3Ljc4UTc5Ljk0IDE4LjE2IDgwLjIyIDE4LjY1UTgwLjUwIDE5LjEzIDgwLjUwIDE5Ljc5TDgwLjUwIDE5Ljc5UTgwLjUwIDIwLjg2IDc5LjY4IDIxLjQ5UTc4Ljg2IDIyLjEyIDc3LjQ2IDIyLjEyTDc3LjQ2IDIyLjEyUTc2LjU0IDIyLjEyIDc1Ljc2IDIxLjc3UTc0Ljk4IDIxLjQzIDc0LjU1IDIwLjgzUTc0LjEyIDIwLjIyIDc0LjEyIDE5LjQyWiIgZmlsbD0iIzAwMDAwMCIvPjxwYXRoIGNsYXNzPSJzdmdfX3RleHQiIGQ9IiIgZmlsbD0iIzAwMDAwMCIgeD0iMTA1LjI4Ii8+PC9zdmc+)](https://novelmovementcph.streamlit.app/Results_%F0%9F%93%8A)
[![forthebadge](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMjUuNjMiIGhlaWdodD0iMzUiIHZpZXdCb3g9IjAgMCAxMjUuNjMgMzUiPjxyZWN0IGNsYXNzPSJzdmdfX3JlY3QiIHg9IjAiIHk9IjAiIHdpZHRoPSIxMjUuNjMiIGhlaWdodD0iMzUiIGZpbGw9IiNBMUExQTEiLz48cmVjdCBjbGFzcz0ic3ZnX19yZWN0IiB4PSIxMjUuNjMiIHk9IjAiIHdpZHRoPSIwIiBoZWlnaHQ9IjM1IiBmaWxsPSIjNkZDMkRFIi8+PHBhdGggY2xhc3M9InN2Z19fdGV4dCIgZD0iTTEzLjk1IDE4LjE5TDEzLjk1IDE4LjE5TDEzLjk1IDE3LjM5UTEzLjk1IDE2LjE5IDE0LjM4IDE1LjI3UTE0LjgwIDE0LjM1IDE1LjYwIDEzLjg1UTE2LjQwIDEzLjM1IDE3LjQ1IDEzLjM1TDE3LjQ1IDEzLjM1UTE4Ljg2IDEzLjM1IDE5LjczIDE0LjEyUTIwLjU5IDE0Ljg5IDIwLjczIDE2LjI5TDIwLjczIDE2LjI5TDE5LjI1IDE2LjI5UTE5LjE0IDE1LjM3IDE4LjcxIDE0Ljk2UTE4LjI4IDE0LjU1IDE3LjQ1IDE0LjU1TDE3LjQ1IDE0LjU1UTE2LjQ4IDE0LjU1IDE1Ljk3IDE1LjI2UTE1LjQ1IDE1Ljk2IDE1LjQ0IDE3LjMzTDE1LjQ0IDE3LjMzTDE1LjQ0IDE4LjA5UTE1LjQ0IDE5LjQ3IDE1LjkzIDIwLjIwUTE2LjQzIDIwLjkyIDE3LjM4IDIwLjkyTDE3LjM4IDIwLjkyUTE4LjI1IDIwLjkyIDE4LjY5IDIwLjUzUTE5LjEzIDIwLjE0IDE5LjI1IDE5LjIyTDE5LjI1IDE5LjIyTDIwLjczIDE5LjIyUTIwLjYwIDIwLjU5IDE5LjcyIDIxLjM1UTE4Ljg0IDIyLjEyIDE3LjM4IDIyLjEyTDE3LjM4IDIyLjEyUTE2LjM2IDIyLjEyIDE1LjU5IDIxLjYzUTE0LjgxIDIxLjE1IDE0LjM5IDIwLjI2UTEzLjk3IDE5LjM3IDEzLjk1IDE4LjE5Wk0yNC43NyAxOC4wMEwyNC43NyAxOC4wMEwyNC43NyAxNy41MlEyNC43NyAxNi4yOCAyNS4yMSAxNS4zMlEyNS42NSAxNC4zNyAyNi40NiAxMy44NlEyNy4yNyAxMy4zNSAyOC4zMSAxMy4zNVEyOS4zNSAxMy4zNSAzMC4xNiAxMy44NVEzMC45NiAxNC4zNSAzMS40MCAxNS4yOVEzMS44NCAxNi4yMyAzMS44NSAxNy40OEwzMS44NSAxNy40OEwzMS44NSAxNy45NlEzMS44NSAxOS4yMSAzMS40MSAyMC4xNlEzMC45OCAyMS4xMCAzMC4xOCAyMS42MVEyOS4zNyAyMi4xMiAyOC4zMiAyMi4xMkwyOC4zMiAyMi4xMlEyNy4yOCAyMi4xMiAyNi40NyAyMS42MVEyNS42NiAyMS4xMCAyNS4yMiAyMC4xN1EyNC43OCAxOS4yMyAyNC43NyAxOC4wMFpNMjYuMjUgMTcuNDZMMjYuMjUgMTcuOTZRMjYuMjUgMTkuMzYgMjYuODAgMjAuMTNRMjcuMzUgMjAuOTAgMjguMzIgMjAuOTBMMjguMzIgMjAuOTBRMjkuMzEgMjAuOTAgMjkuODQgMjAuMTVRMzAuMzcgMTkuNDAgMzAuMzcgMTcuOTZMMzAuMzcgMTcuOTZMMzAuMzcgMTcuNTFRMzAuMzcgMTYuMDkgMjkuODMgMTUuMzRRMjkuMjkgMTQuNTggMjguMzEgMTQuNThMMjguMzEgMTQuNThRMjcuMzUgMTQuNTggMjYuODEgMTUuMzNRMjYuMjYgMTYuMDkgMjYuMjUgMTcuNDZMMjYuMjUgMTcuNDZaTTM3LjgwIDIyTDM2LjMxIDIyTDM2LjMxIDEzLjQ3TDM3LjgwIDEzLjQ3TDQxLjYxIDE5LjU0TDQxLjYxIDEzLjQ3TDQzLjA4IDEzLjQ3TDQzLjA4IDIyTDQxLjYwIDIyTDM3LjgwIDE1Ljk1TDM3LjgwIDIyWk00Ny41NSAxOC4xOUw0Ny41NSAxOC4xOUw0Ny41NSAxNy4zOVE0Ny41NSAxNi4xOSA0Ny45OCAxNS4yN1E0OC40MSAxNC4zNSA0OS4yMSAxMy44NVE1MC4wMSAxMy4zNSA1MS4wNiAxMy4zNUw1MS4wNiAxMy4zNVE1Mi40NyAxMy4zNSA1My4zMyAxNC4xMlE1NC4xOSAxNC44OSA1NC4zMyAxNi4yOUw1NC4zMyAxNi4yOUw1Mi44NSAxNi4yOVE1Mi43NSAxNS4zNyA1Mi4zMiAxNC45NlE1MS44OSAxNC41NSA1MS4wNiAxNC41NUw1MS4wNiAxNC41NVE1MC4wOSAxNC41NSA0OS41NyAxNS4yNlE0OS4wNSAxNS45NiA0OS4wNCAxNy4zM0w0OS4wNCAxNy4zM0w0OS4wNCAxOC4wOVE0OS4wNCAxOS40NyA0OS41MyAyMC4yMFE1MC4wMyAyMC45MiA1MC45OCAyMC45Mkw1MC45OCAyMC45MlE1MS44NiAyMC45MiA1Mi4zMCAyMC41M1E1Mi43NCAyMC4xNCA1Mi44NSAxOS4yMkw1Mi44NSAxOS4yMkw1NC4zMyAxOS4yMlE1NC4yMCAyMC41OSA1My4zMiAyMS4zNVE1Mi40NCAyMi4xMiA1MC45OCAyMi4xMkw1MC45OCAyMi4xMlE0OS45NyAyMi4xMiA0OS4xOSAyMS42M1E0OC40MSAyMS4xNSA0Ny45OSAyMC4yNlE0Ny41NyAxOS4zNyA0Ny41NSAxOC4xOVpNNjQuMDAgMjJMNTguNjQgMjJMNTguNjQgMTMuNDdMNjAuMTMgMTMuNDdMNjAuMTMgMjAuODJMNjQuMDAgMjAuODJMNjQuMDAgMjJaTTY3Ljk5IDE5LjE2TDY3Ljk5IDE5LjE2TDY3Ljk5IDEzLjQ3TDY5LjQ3IDEzLjQ3TDY5LjQ3IDE5LjE4UTY5LjQ3IDIwLjAzIDY5LjkwIDIwLjQ4UTcwLjMzIDIwLjkzIDcxLjE4IDIwLjkzTDcxLjE4IDIwLjkzUTcyLjg5IDIwLjkzIDcyLjg5IDE5LjEzTDcyLjg5IDE5LjEzTDcyLjg5IDEzLjQ3TDc0LjM2IDEzLjQ3TDc0LjM2IDE5LjE3UTc0LjM2IDIwLjUzIDczLjQ5IDIxLjMyUTcyLjYyIDIyLjEyIDcxLjE4IDIyLjEyTDcxLjE4IDIyLjEyUTY5LjcxIDIyLjEyIDY4Ljg1IDIxLjMzUTY3Ljk5IDIwLjU1IDY3Ljk5IDE5LjE2Wk03OC41MCAxOS40Mkw3OC41MCAxOS40Mkw3OS45OCAxOS40MlE3OS45OCAyMC4xNSA4MC40NiAyMC41NVE4MC45NCAyMC45NSA4MS44NCAyMC45NUw4MS44NCAyMC45NVE4Mi42MSAyMC45NSA4My4wMCAyMC42M1E4My4zOSAyMC4zMiA4My4zOSAxOS44MEw4My4zOSAxOS44MFE4My4zOSAxOS4yNCA4My4wMCAxOC45NFE4Mi42MCAxOC42MyA4MS41NyAxOC4zMlE4MC41NCAxOC4wMSA3OS45MyAxNy42M0w3OS45MyAxNy42M1E3OC43NiAxNi45MCA3OC43NiAxNS43Mkw3OC43NiAxNS43MlE3OC43NiAxNC42OSA3OS42MCAxNC4wMlE4MC40NSAxMy4zNSA4MS43OSAxMy4zNUw4MS43OSAxMy4zNVE4Mi42OCAxMy4zNSA4My4zOCAxMy42OFE4NC4wNyAxNC4wMSA4NC40NyAxNC42MVE4NC44NyAxNS4yMiA4NC44NyAxNS45Nkw4NC44NyAxNS45Nkw4My4zOSAxNS45NlE4My4zOSAxNS4yOSA4Mi45NyAxNC45MVE4Mi41NiAxNC41NCA4MS43OCAxNC41NEw4MS43OCAxNC41NFE4MS4wNSAxNC41NCA4MC42NSAxNC44NVE4MC4yNSAxNS4xNiA4MC4yNSAxNS43MUw4MC4yNSAxNS43MVE4MC4yNSAxNi4xOCA4MC42OCAxNi41MFE4MS4xMSAxNi44MSA4Mi4xMSAxNy4xMFE4My4xMSAxNy40MCA4My43MSAxNy43OFE4NC4zMSAxOC4xNiA4NC41OSAxOC42NVE4NC44OCAxOS4xMyA4NC44OCAxOS43OUw4NC44OCAxOS43OVE4NC44OCAyMC44NiA4NC4wNiAyMS40OVE4My4yNCAyMi4xMiA4MS44NCAyMi4xMkw4MS44NCAyMi4xMlE4MC45MSAyMi4xMiA4MC4xNCAyMS43N1E3OS4zNiAyMS40MyA3OC45MyAyMC44M1E3OC41MCAyMC4yMiA3OC41MCAxOS40MlpNOTAuNzMgMjJMODkuMjUgMjJMODkuMjUgMTMuNDdMOTAuNzMgMTMuNDdMOTAuNzMgMjJaTTk1LjI3IDE4LjAwTDk1LjI3IDE4LjAwTDk1LjI3IDE3LjUyUTk1LjI3IDE2LjI4IDk1LjcxIDE1LjMyUTk2LjE1IDE0LjM3IDk2Ljk2IDEzLjg2UTk3Ljc3IDEzLjM1IDk4LjgxIDEzLjM1UTk5Ljg1IDEzLjM1IDEwMC42NiAxMy44NVExMDEuNDYgMTQuMzUgMTAxLjkwIDE1LjI5UTEwMi4zNCAxNi4yMyAxMDIuMzUgMTcuNDhMMTAyLjM1IDE3LjQ4TDEwMi4zNSAxNy45NlExMDIuMzUgMTkuMjEgMTAxLjkxIDIwLjE2UTEwMS40OCAyMS4xMCAxMDAuNjggMjEuNjFROTkuODcgMjIuMTIgOTguODIgMjIuMTJMOTguODIgMjIuMTJROTcuNzggMjIuMTIgOTYuOTcgMjEuNjFROTYuMTYgMjEuMTAgOTUuNzIgMjAuMTdROTUuMjggMTkuMjMgOTUuMjcgMTguMDBaTTk2Ljc1IDE3LjQ2TDk2Ljc1IDE3Ljk2UTk2Ljc1IDE5LjM2IDk3LjMwIDIwLjEzUTk3Ljg1IDIwLjkwIDk4LjgyIDIwLjkwTDk4LjgyIDIwLjkwUTk5LjgxIDIwLjkwIDEwMC4zNCAyMC4xNVExMDAuODcgMTkuNDAgMTAwLjg3IDE3Ljk2TDEwMC44NyAxNy45NkwxMDAuODcgMTcuNTFRMTAwLjg3IDE2LjA5IDEwMC4zMyAxNS4zNFE5OS43OSAxNC41OCA5OC44MSAxNC41OEw5OC44MSAxNC41OFE5Ny44NSAxNC41OCA5Ny4zMSAxNS4zM1E5Ni43NiAxNi4wOSA5Ni43NSAxNy40Nkw5Ni43NSAxNy40NlpNMTA4LjMwIDIyTDEwNi44MSAyMkwxMDYuODEgMTMuNDdMMTA4LjMwIDEzLjQ3TDExMi4xMSAxOS41NEwxMTIuMTEgMTMuNDdMMTEzLjU4IDEzLjQ3TDExMy41OCAyMkwxMTIuMTAgMjJMMTA4LjMwIDE1Ljk1TDEwOC4zMCAyMloiIGZpbGw9IiMwMDAwMDAiLz48cGF0aCBjbGFzcz0ic3ZnX190ZXh0IiBkPSIiIGZpbGw9IiMwMDAwMDAiIHg9IjEzOC42MyIvPjwvc3ZnPg==)](https://novelmovementcph.streamlit.app/Conclusion_%F0%9F%92%8A)
"""
st.title("Introduction")
topside1, topside2 = st.columns([1.5, 1])
topside1.markdown(
"""
Cervical-level spinal cord injury (SCI) negatively impacts upper extremity (UE) function to varying degrees and typically results in reduced independence or tetraplegia [1]. 

The Capabilities of Upper Extremity Test (CUE-T) was developed to capture UE function through different arm and hand tasks in individuals with tetraplegia and has been established as an accurate clinical assessment [2]. While clinical assessments capture cross-sectional information, there is a demand for technologies that can passively monitor UE function without the need for clinicians and researchers in the community. 

"""
)
we = "https://raw.githubusercontent.com/chags1313/cphresearchday/main/wheelchairexercise.jpg"
topside2.image(we, use_column_width=True, caption = 'AI generated image')
"""
Novelty detection is one such method that provides key ingredients to identify and monitor UE function over time, especially when paired with real-world monitoring devices such as wearable sensors. In general, novelty detection is a semi-supervised machine learning technique used to identify characteristics of data samples collected during a baseline assessment and then used on new data samples to recognize characteristics that appear different or new [3]. 

Novelty detection methods have been used in previous research with movement data, including wearable-sensor-captured movement data, to monitor clinically relevant outcomes, such as gait, falls, and abnormal movements [3-5]. To our knowledge, novelty detection methods have not been applied to movement data collected from individuals with SCI. Previous research in SCI has used multiple wearable sensors to detect and classify physical activities or quantify movement kinematics [6,7]. While these metrics are useful in understanding the magnitude and frequency of physical movement, they lack critical context regarding when and how function recovers over time. 

"""
st.title("Objective")
"""
The overarching goal of this study is to assess the relationship between novel UE movement pattern scores identified through novelty detection methods and clinical UE function scores as measured by the CUE-T. 
"""

spacer1, spacer2, spacer3 = st.columns(3)

spacer2.markdown(
"""
[![forthebadge](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMzAuMyIgaGVpZ2h0PSIzNSIgdmlld0JveD0iMCAwIDEzMC4zIDM1Ij48cmVjdCBjbGFzcz0ic3ZnX19yZWN0IiB4PSIwIiB5PSIwIiB3aWR0aD0iMTAwLjM5IiBoZWlnaHQ9IjM1IiBmaWxsPSIjMDAwMDAwIi8+PHJlY3QgY2xhc3M9InN2Z19fcmVjdCIgeD0iOTguMzkiIHk9IjAiIHdpZHRoPSIzMS45MDk5OTk5OTk5OTk5OTciIGhlaWdodD0iMzUiIGZpbGw9IiMzQzlBRDUiLz48cGF0aCBjbGFzcz0ic3ZnX190ZXh0IiBkPSJNMTUuNjkgMjJMMTQuMjIgMjJMMTQuMjIgMTMuNDdMMTYuMTQgMTMuNDdMMTguNjAgMjAuMDFMMjEuMDYgMTMuNDdMMjIuOTcgMTMuNDdMMjIuOTcgMjJMMjEuNDkgMjJMMjEuNDkgMTkuMTlMMjEuNjQgMTUuNDNMMTkuMTIgMjJMMTguMDYgMjJMMTUuNTUgMTUuNDNMMTUuNjkgMTkuMTlMMTUuNjkgMjJaTTMzLjI5IDIyTDI3LjcxIDIyTDI3LjcxIDEzLjQ3TDMzLjI1IDEzLjQ3TDMzLjI1IDE0LjY2TDI5LjE5IDE0LjY2TDI5LjE5IDE3LjAyTDMyLjcwIDE3LjAyTDMyLjcwIDE4LjE5TDI5LjE5IDE4LjE5TDI5LjE5IDIwLjgyTDMzLjI5IDIwLjgyTDMzLjI5IDIyWk0zOS4xNyAxNC42NkwzNi41MyAxNC42NkwzNi41MyAxMy40N0w0My4zMCAxMy40N0w0My4zMCAxNC42Nkw0MC42NCAxNC42Nkw0MC42NCAyMkwzOS4xNyAyMkwzOS4xNyAxNC42NlpNNDguNTQgMjJMNDcuMDUgMjJMNDcuMDUgMTMuNDdMNDguNTQgMTMuNDdMNDguNTQgMTcuMDJMNTIuMzUgMTcuMDJMNTIuMzUgMTMuNDdMNTMuODMgMTMuNDdMNTMuODMgMjJMNTIuMzUgMjJMNTIuMzUgMTguMjFMNDguNTQgMTguMjFMNDguNTQgMjJaTTU4LjMwIDE4LjAwTDU4LjMwIDE4LjAwTDU4LjMwIDE3LjUyUTU4LjMwIDE2LjI4IDU4Ljc0IDE1LjMyUTU5LjE4IDE0LjM3IDU5Ljk5IDEzLjg2UTYwLjc5IDEzLjM1IDYxLjg0IDEzLjM1UTYyLjg4IDEzLjM1IDYzLjY4IDEzLjg1UTY0LjQ5IDE0LjM1IDY0LjkzIDE1LjI5UTY1LjM3IDE2LjIzIDY1LjM4IDE3LjQ4TDY1LjM4IDE3LjQ4TDY1LjM4IDE3Ljk2UTY1LjM4IDE5LjIxIDY0Ljk0IDIwLjE2UTY0LjUxIDIxLjEwIDYzLjcwIDIxLjYxUTYyLjkwIDIyLjEyIDYxLjg1IDIyLjEyTDYxLjg1IDIyLjEyUTYwLjgxIDIyLjEyIDYwLjAwIDIxLjYxUTU5LjE5IDIxLjEwIDU4Ljc1IDIwLjE3UTU4LjMwIDE5LjIzIDU4LjMwIDE4LjAwWk01OS43OCAxNy40Nkw1OS43OCAxNy45NlE1OS43OCAxOS4zNiA2MC4zMyAyMC4xM1E2MC44OCAyMC45MCA2MS44NSAyMC45MEw2MS44NSAyMC45MFE2Mi44MyAyMC45MCA2My4zNiAyMC4xNVE2My44OSAxOS40MCA2My44OSAxNy45Nkw2My44OSAxNy45Nkw2My44OSAxNy41MVE2My44OSAxNi4wOSA2My4zNiAxNS4zNFE2Mi44MiAxNC41OCA2MS44NCAxNC41OEw2MS44NCAxNC41OFE2MC44OCAxNC41OCA2MC4zMyAxNS4zM1E1OS43OSAxNi4wOSA1OS43OCAxNy40Nkw1OS43OCAxNy40NlpNNzIuMzAgMjJMNjkuODQgMjJMNjkuODQgMTMuNDdMNzIuMzYgMTMuNDdRNzMuNDkgMTMuNDcgNzQuMzcgMTMuOTdRNzUuMjQgMTQuNDggNzUuNzIgMTUuNDBRNzYuMjAgMTYuMzMgNzYuMjAgMTcuNTJMNzYuMjAgMTcuNTJMNzYuMjAgMTcuOTVRNzYuMjAgMTkuMTYgNzUuNzIgMjAuMDhRNzUuMjQgMjEuMDAgNzQuMzQgMjEuNTBRNzMuNDUgMjIgNzIuMzAgMjJMNzIuMzAgMjJaTTcxLjMyIDE0LjY2TDcxLjMyIDIwLjgyTDcyLjI5IDIwLjgyUTczLjQ2IDIwLjgyIDc0LjA4IDIwLjA5UTc0LjcwIDE5LjM2IDc0LjcyIDE3Ljk5TDc0LjcyIDE3Ljk5TDc0LjcyIDE3LjUyUTc0LjcyIDE2LjEzIDc0LjExIDE1LjQwUTczLjUxIDE0LjY2IDcyLjM2IDE0LjY2TDcyLjM2IDE0LjY2TDcxLjMyIDE0LjY2Wk04MC4yMyAxOS40Mkw4MC4yMyAxOS40Mkw4MS43MiAxOS40MlE4MS43MiAyMC4xNSA4Mi4yMCAyMC41NVE4Mi42OCAyMC45NSA4My41NyAyMC45NUw4My41NyAyMC45NVE4NC4zNSAyMC45NSA4NC43NCAyMC42M1E4NS4xMyAyMC4zMiA4NS4xMyAxOS44MEw4NS4xMyAxOS44MFE4NS4xMyAxOS4yNCA4NC43MyAxOC45NFE4NC4zNCAxOC42MyA4My4zMSAxOC4zMlE4Mi4yNyAxOC4wMSA4MS42NiAxNy42M0w4MS42NiAxNy42M1E4MC41MCAxNi45MCA4MC41MCAxNS43Mkw4MC41MCAxNS43MlE4MC41MCAxNC42OSA4MS4zNCAxNC4wMlE4Mi4xOCAxMy4zNSA4My41MiAxMy4zNUw4My41MiAxMy4zNVE4NC40MSAxMy4zNSA4NS4xMSAxMy42OFE4NS44MSAxNC4wMSA4Ni4yMSAxNC42MVE4Ni42MCAxNS4yMiA4Ni42MCAxNS45Nkw4Ni42MCAxNS45Nkw4NS4xMyAxNS45NlE4NS4xMyAxNS4yOSA4NC43MSAxNC45MVE4NC4yOSAxNC41NCA4My41MSAxNC41NEw4My41MSAxNC41NFE4Mi43OCAxNC41NCA4Mi4zOCAxNC44NVE4MS45OCAxNS4xNiA4MS45OCAxNS43MUw4MS45OCAxNS43MVE4MS45OCAxNi4xOCA4Mi40MSAxNi41MFE4Mi44NSAxNi44MSA4My44NCAxNy4xMFE4NC44NCAxNy40MCA4NS40NCAxNy43OFE4Ni4wNSAxOC4xNiA4Ni4zMyAxOC42NVE4Ni42MSAxOS4xMyA4Ni42MSAxOS43OUw4Ni42MSAxOS43OVE4Ni42MSAyMC44NiA4NS43OSAyMS40OVE4NC45NyAyMi4xMiA4My41NyAyMi4xMkw4My41NyAyMi4xMlE4Mi42NSAyMi4xMiA4MS44NyAyMS43N1E4MS4xMCAyMS40MyA4MC42NyAyMC44M1E4MC4yMyAyMC4yMiA4MC4yMyAxOS40MloiIGZpbGw9IiNGRkZGRkYiLz48cGF0aCBjbGFzcz0ic3ZnX190ZXh0IiBkPSJNMTE4LjM1IDE4LjcyTDExMi40NCAyMC45MUwxMTIuNDQgMTkuMTZMMTE2LjI2IDE3LjgwTDExMi40NCAxNi40NUwxMTIuNDQgMTQuNjlMMTE4LjM1IDE2Ljg4TDExOC4zNSAxOC43MloiIGZpbGw9IiMwMDAwMDAiIHg9IjExMS4zOSIvPjwvc3ZnPg==)](https://novelmovementcph.streamlit.app/Methods_%E2%9C%8F%EF%B8%8F_)
""")
