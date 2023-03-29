import streamlit as st
from PIL import Image
import pandas as pd
data = pd.read_pickle("https://raw.githubusercontent.com/chags1313/cphresearchday/main/pages/alld.pkl")
"""
[![forthebadge](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNDEuNTUiIGhlaWdodD0iMzUiIHZpZXdCb3g9IjAgMCAxNDEuNTUgMzUiPjxyZWN0IGNsYXNzPSJzdmdfX3JlY3QiIHg9IjAiIHk9IjAiIHdpZHRoPSIxNDEuNTUiIGhlaWdodD0iMzUiIGZpbGw9IiNBMUExQTEiLz48cmVjdCBjbGFzcz0ic3ZnX19yZWN0IiB4PSIxNDEuNTUiIHk9IjAiIHdpZHRoPSIwIiBoZWlnaHQ9IjM1IiBmaWxsPSIjNkZDMkRFIi8+PHBhdGggY2xhc3M9InN2Z19fdGV4dCIgZD0iTTE1Ljc4IDIyTDE0LjMxIDIyTDE0LjMxIDEzLjQ3TDE1Ljc4IDEzLjQ3TDE1Ljc4IDIyWk0yMi4wNyAyMkwyMC41OSAyMkwyMC41OSAxMy40N0wyMi4wNyAxMy40N0wyNS44OSAxOS41NEwyNS44OSAxMy40N0wyNy4zNiAxMy40N0wyNy4zNiAyMkwyNS44OCAyMkwyMi4wNyAxNS45NUwyMi4wNyAyMlpNMzMuNzggMTQuNjZMMzEuMTQgMTQuNjZMMzEuMTQgMTMuNDdMMzcuOTEgMTMuNDdMMzcuOTEgMTQuNjZMMzUuMjUgMTQuNjZMMzUuMjUgMjJMMzMuNzggMjJMMzMuNzggMTQuNjZaTTQzLjE1IDIyTDQxLjY3IDIyTDQxLjY3IDEzLjQ3TDQ0LjY3IDEzLjQ3UTQ2LjE0IDEzLjQ3IDQ2Ljk1IDE0LjEzUTQ3Ljc1IDE0Ljc5IDQ3Ljc1IDE2LjA1TDQ3Ljc1IDE2LjA1UTQ3Ljc1IDE2LjkwIDQ3LjM0IDE3LjQ4UTQ2LjkyIDE4LjA2IDQ2LjE5IDE4LjM3TDQ2LjE5IDE4LjM3TDQ4LjEwIDIxLjkyTDQ4LjEwIDIyTDQ2LjUxIDIyTDQ0LjgwIDE4LjcxTDQzLjE1IDE4LjcxTDQzLjE1IDIyWk00My4xNSAxNC42Nkw0My4xNSAxNy41Mkw0NC42NyAxNy41MlE0NS40MiAxNy41MiA0NS44NSAxNy4xNVE0Ni4yNyAxNi43NyA0Ni4yNyAxNi4xMUw0Ni4yNyAxNi4xMVE0Ni4yNyAxNS40MyA0NS44OCAxNS4wNVE0NS40OSAxNC42OCA0NC43MiAxNC42Nkw0NC43MiAxNC42Nkw0My4xNSAxNC42NlpNNTEuODggMTguMDBMNTEuODggMTguMDBMNTEuODggMTcuNTJRNTEuODggMTYuMjggNTIuMzIgMTUuMzJRNTIuNzYgMTQuMzcgNTMuNTcgMTMuODZRNTQuMzcgMTMuMzUgNTUuNDEgMTMuMzVRNTYuNDYgMTMuMzUgNTcuMjYgMTMuODVRNTguMDcgMTQuMzUgNTguNTEgMTUuMjlRNTguOTUgMTYuMjMgNTguOTUgMTcuNDhMNTguOTUgMTcuNDhMNTguOTUgMTcuOTZRNTguOTUgMTkuMjEgNTguNTIgMjAuMTZRNTguMDkgMjEuMTAgNTcuMjggMjEuNjFRNTYuNDggMjIuMTIgNTUuNDMgMjIuMTJMNTUuNDMgMjIuMTJRNTQuMzkgMjIuMTIgNTMuNTggMjEuNjFRNTIuNzcgMjEuMTAgNTIuMzIgMjAuMTdRNTEuODggMTkuMjMgNTEuODggMTguMDBaTTUzLjM2IDE3LjQ2TDUzLjM2IDE3Ljk2UTUzLjM2IDE5LjM2IDUzLjkxIDIwLjEzUTU0LjQ1IDIwLjkwIDU1LjQzIDIwLjkwTDU1LjQzIDIwLjkwUTU2LjQxIDIwLjkwIDU2Ljk0IDIwLjE1UTU3LjQ3IDE5LjQwIDU3LjQ3IDE3Ljk2TDU3LjQ3IDE3Ljk2TDU3LjQ3IDE3LjUxUTU3LjQ3IDE2LjA5IDU2LjkzIDE1LjM0UTU2LjQwIDE0LjU4IDU1LjQxIDE0LjU4TDU1LjQxIDE0LjU4UTU0LjQ1IDE0LjU4IDUzLjkxIDE1LjMzUTUzLjM3IDE2LjA5IDUzLjM2IDE3LjQ2TDUzLjM2IDE3LjQ2Wk02NS44NyAyMkw2My40MiAyMkw2My40MiAxMy40N0w2NS45NCAxMy40N1E2Ny4wNyAxMy40NyA2Ny45NCAxMy45N1E2OC44MiAxNC40OCA2OS4zMCAxNS40MFE2OS43OCAxNi4zMyA2OS43OCAxNy41Mkw2OS43OCAxNy41Mkw2OS43OCAxNy45NVE2OS43OCAxOS4xNiA2OS4zMCAyMC4wOFE2OC44MSAyMS4wMCA2Ny45MiAyMS41MFE2Ny4wMyAyMiA2NS44NyAyMkw2NS44NyAyMlpNNjQuOTAgMTQuNjZMNjQuOTAgMjAuODJMNjUuODcgMjAuODJRNjcuMDMgMjAuODIgNjcuNjYgMjAuMDlRNjguMjggMTkuMzYgNjguMjkgMTcuOTlMNjguMjkgMTcuOTlMNjguMjkgMTcuNTJRNjguMjkgMTYuMTMgNjcuNjkgMTUuNDBRNjcuMDkgMTQuNjYgNjUuOTQgMTQuNjZMNjUuOTQgMTQuNjZMNjQuOTAgMTQuNjZaTTc0LjExIDE5LjE2TDc0LjExIDE5LjE2TDc0LjExIDEzLjQ3TDc1LjU5IDEzLjQ3TDc1LjU5IDE5LjE4UTc1LjU5IDIwLjAzIDc2LjAyIDIwLjQ4UTc2LjQ2IDIwLjkzIDc3LjMwIDIwLjkzTDc3LjMwIDIwLjkzUTc5LjAxIDIwLjkzIDc5LjAxIDE5LjEzTDc5LjAxIDE5LjEzTDc5LjAxIDEzLjQ3TDgwLjQ5IDEzLjQ3TDgwLjQ5IDE5LjE3UTgwLjQ5IDIwLjUzIDc5LjYyIDIxLjMyUTc4Ljc1IDIyLjEyIDc3LjMwIDIyLjEyTDc3LjMwIDIyLjEyUTc1LjgzIDIyLjEyIDc0Ljk3IDIxLjMzUTc0LjExIDIwLjU1IDc0LjExIDE5LjE2Wk04NC43OSAxOC4xOUw4NC43OSAxOC4xOUw4NC43OSAxNy4zOVE4NC43OSAxNi4xOSA4NS4yMiAxNS4yN1E4NS42NCAxNC4zNSA4Ni40NCAxMy44NVE4Ny4yNCAxMy4zNSA4OC4yOSAxMy4zNUw4OC4yOSAxMy4zNVE4OS43MCAxMy4zNSA5MC41NiAxNC4xMlE5MS40MyAxNC44OSA5MS41NyAxNi4yOUw5MS41NyAxNi4yOUw5MC4wOSAxNi4yOVE4OS45OCAxNS4zNyA4OS41NSAxNC45NlE4OS4xMiAxNC41NSA4OC4yOSAxNC41NUw4OC4yOSAxNC41NVE4Ny4zMiAxNC41NSA4Ni44MSAxNS4yNlE4Ni4yOSAxNS45NiA4Ni4yOCAxNy4zM0w4Ni4yOCAxNy4zM0w4Ni4yOCAxOC4wOVE4Ni4yOCAxOS40NyA4Ni43NyAyMC4yMFE4Ny4yNyAyMC45MiA4OC4yMiAyMC45Mkw4OC4yMiAyMC45MlE4OS4wOSAyMC45MiA4OS41MyAyMC41M1E4OS45NyAyMC4xNCA5MC4wOSAxOS4yMkw5MC4wOSAxOS4yMkw5MS41NyAxOS4yMlE5MS40NCAyMC41OSA5MC41NiAyMS4zNVE4OS42OCAyMi4xMiA4OC4yMiAyMi4xMkw4OC4yMiAyMi4xMlE4Ny4yMCAyMi4xMiA4Ni40MyAyMS42M1E4NS42NSAyMS4xNSA4NS4yMyAyMC4yNlE4NC44MSAxOS4zNyA4NC43OSAxOC4xOVpNOTcuNTYgMTQuNjZMOTQuOTIgMTQuNjZMOTQuOTIgMTMuNDdMMTAxLjY5IDEzLjQ3TDEwMS42OSAxNC42Nkw5OS4wMyAxNC42Nkw5OS4wMyAyMkw5Ny41NiAyMkw5Ny41NiAxNC42NlpNMTA3LjAxIDIyTDEwNS41NCAyMkwxMDUuNTQgMTMuNDdMMTA3LjAxIDEzLjQ3TDEwNy4wMSAyMlpNMTExLjU1IDE4LjAwTDExMS41NSAxOC4wMEwxMTEuNTUgMTcuNTJRMTExLjU1IDE2LjI4IDExMi4wMCAxNS4zMlExMTIuNDQgMTQuMzcgMTEzLjI0IDEzLjg2UTExNC4wNSAxMy4zNSAxMTUuMDkgMTMuMzVRMTE2LjE0IDEzLjM1IDExNi45NCAxMy44NVExMTcuNzUgMTQuMzUgMTE4LjE5IDE1LjI5UTExOC42MyAxNi4yMyAxMTguNjMgMTcuNDhMMTE4LjYzIDE3LjQ4TDExOC42MyAxNy45NlExMTguNjMgMTkuMjEgMTE4LjIwIDIwLjE2UTExNy43NiAyMS4xMCAxMTYuOTYgMjEuNjFRMTE2LjE1IDIyLjEyIDExNS4xMCAyMi4xMkwxMTUuMTAgMjIuMTJRMTE0LjA3IDIyLjEyIDExMy4yNiAyMS42MVExMTIuNDQgMjEuMTAgMTEyLjAwIDIwLjE3UTExMS41NiAxOS4yMyAxMTEuNTUgMTguMDBaTTExMy4wNCAxNy40NkwxMTMuMDQgMTcuOTZRMTEzLjA0IDE5LjM2IDExMy41OCAyMC4xM1ExMTQuMTMgMjAuOTAgMTE1LjEwIDIwLjkwTDExNS4xMCAyMC45MFExMTYuMDkgMjAuOTAgMTE2LjYyIDIwLjE1UTExNy4xNSAxOS40MCAxMTcuMTUgMTcuOTZMMTE3LjE1IDE3Ljk2TDExNy4xNSAxNy41MVExMTcuMTUgMTYuMDkgMTE2LjYxIDE1LjM0UTExNi4wOCAxNC41OCAxMTUuMDkgMTQuNThMMTE1LjA5IDE0LjU4UTExNC4xMyAxNC41OCAxMTMuNTkgMTUuMzNRMTEzLjA1IDE2LjA5IDExMy4wNCAxNy40NkwxMTMuMDQgMTcuNDZaTTEyNC41OCAyMkwxMjMuMTAgMjJMMTIzLjEwIDEzLjQ3TDEyNC41OCAxMy40N0wxMjguMzkgMTkuNTRMMTI4LjM5IDEzLjQ3TDEyOS44NiAxMy40N0wxMjkuODYgMjJMMTI4LjM4IDIyTDEyNC41OCAxNS45NUwxMjQuNTggMjJaIiBmaWxsPSIjMDAwMDAwIi8+PHBhdGggY2xhc3M9InN2Z19fdGV4dCIgZD0iIiBmaWxsPSIjMDAwMDAwIiB4PSIxNTQuNTUiLz48L3N2Zz4=)](https://novelmovementcph.streamlit.app/Introduction_%F0%9F%8F%A0)
[![forthebadge](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI5OC4zOSIgaGVpZ2h0PSIzNSIgdmlld0JveD0iMCAwIDk4LjM5IDM1Ij48cmVjdCBjbGFzcz0ic3ZnX19yZWN0IiB4PSIwIiB5PSIwIiB3aWR0aD0iOTguMzkiIGhlaWdodD0iMzUiIGZpbGw9IiMzQzlBRDUiLz48cmVjdCBjbGFzcz0ic3ZnX19yZWN0IiB4PSI5OC4zOSIgeT0iMCIgd2lkdGg9IjAiIGhlaWdodD0iMzUiIGZpbGw9IiM2RkMyREUiLz48cGF0aCBjbGFzcz0ic3ZnX190ZXh0IiBkPSJNMTUuNjkgMjJMMTQuMjIgMjJMMTQuMjIgMTMuNDdMMTYuMTQgMTMuNDdMMTguNjAgMjAuMDFMMjEuMDYgMTMuNDdMMjIuOTcgMTMuNDdMMjIuOTcgMjJMMjEuNDkgMjJMMjEuNDkgMTkuMTlMMjEuNjQgMTUuNDNMMTkuMTIgMjJMMTguMDYgMjJMMTUuNTUgMTUuNDNMMTUuNjkgMTkuMTlMMTUuNjkgMjJaTTMzLjI5IDIyTDI3LjcxIDIyTDI3LjcxIDEzLjQ3TDMzLjI1IDEzLjQ3TDMzLjI1IDE0LjY2TDI5LjE5IDE0LjY2TDI5LjE5IDE3LjAyTDMyLjcwIDE3LjAyTDMyLjcwIDE4LjE5TDI5LjE5IDE4LjE5TDI5LjE5IDIwLjgyTDMzLjI5IDIwLjgyTDMzLjI5IDIyWk0zOS4xNyAxNC42NkwzNi41MyAxNC42NkwzNi41MyAxMy40N0w0My4zMCAxMy40N0w0My4zMCAxNC42Nkw0MC42NCAxNC42Nkw0MC42NCAyMkwzOS4xNyAyMkwzOS4xNyAxNC42NlpNNDguNTQgMjJMNDcuMDUgMjJMNDcuMDUgMTMuNDdMNDguNTQgMTMuNDdMNDguNTQgMTcuMDJMNTIuMzUgMTcuMDJMNTIuMzUgMTMuNDdMNTMuODMgMTMuNDdMNTMuODMgMjJMNTIuMzUgMjJMNTIuMzUgMTguMjFMNDguNTQgMTguMjFMNDguNTQgMjJaTTU4LjMwIDE4LjAwTDU4LjMwIDE4LjAwTDU4LjMwIDE3LjUyUTU4LjMwIDE2LjI4IDU4Ljc0IDE1LjMyUTU5LjE4IDE0LjM3IDU5Ljk5IDEzLjg2UTYwLjc5IDEzLjM1IDYxLjg0IDEzLjM1UTYyLjg4IDEzLjM1IDYzLjY4IDEzLjg1UTY0LjQ5IDE0LjM1IDY0LjkzIDE1LjI5UTY1LjM3IDE2LjIzIDY1LjM4IDE3LjQ4TDY1LjM4IDE3LjQ4TDY1LjM4IDE3Ljk2UTY1LjM4IDE5LjIxIDY0Ljk0IDIwLjE2UTY0LjUxIDIxLjEwIDYzLjcwIDIxLjYxUTYyLjkwIDIyLjEyIDYxLjg1IDIyLjEyTDYxLjg1IDIyLjEyUTYwLjgxIDIyLjEyIDYwLjAwIDIxLjYxUTU5LjE5IDIxLjEwIDU4Ljc1IDIwLjE3UTU4LjMwIDE5LjIzIDU4LjMwIDE4LjAwWk01OS43OCAxNy40Nkw1OS43OCAxNy45NlE1OS43OCAxOS4zNiA2MC4zMyAyMC4xM1E2MC44OCAyMC45MCA2MS44NSAyMC45MEw2MS44NSAyMC45MFE2Mi44MyAyMC45MCA2My4zNiAyMC4xNVE2My44OSAxOS40MCA2My44OSAxNy45Nkw2My44OSAxNy45Nkw2My44OSAxNy41MVE2My44OSAxNi4wOSA2My4zNiAxNS4zNFE2Mi44MiAxNC41OCA2MS44NCAxNC41OEw2MS44NCAxNC41OFE2MC44OCAxNC41OCA2MC4zMyAxNS4zM1E1OS43OSAxNi4wOSA1OS43OCAxNy40Nkw1OS43OCAxNy40NlpNNzIuMzAgMjJMNjkuODQgMjJMNjkuODQgMTMuNDdMNzIuMzYgMTMuNDdRNzMuNDkgMTMuNDcgNzQuMzcgMTMuOTdRNzUuMjQgMTQuNDggNzUuNzIgMTUuNDBRNzYuMjAgMTYuMzMgNzYuMjAgMTcuNTJMNzYuMjAgMTcuNTJMNzYuMjAgMTcuOTVRNzYuMjAgMTkuMTYgNzUuNzIgMjAuMDhRNzUuMjQgMjEuMDAgNzQuMzQgMjEuNTBRNzMuNDUgMjIgNzIuMzAgMjJMNzIuMzAgMjJaTTcxLjMyIDE0LjY2TDcxLjMyIDIwLjgyTDcyLjI5IDIwLjgyUTczLjQ2IDIwLjgyIDc0LjA4IDIwLjA5UTc0LjcwIDE5LjM2IDc0LjcyIDE3Ljk5TDc0LjcyIDE3Ljk5TDc0LjcyIDE3LjUyUTc0LjcyIDE2LjEzIDc0LjExIDE1LjQwUTczLjUxIDE0LjY2IDcyLjM2IDE0LjY2TDcyLjM2IDE0LjY2TDcxLjMyIDE0LjY2Wk04MC4yMyAxOS40Mkw4MC4yMyAxOS40Mkw4MS43MiAxOS40MlE4MS43MiAyMC4xNSA4Mi4yMCAyMC41NVE4Mi42OCAyMC45NSA4My41NyAyMC45NUw4My41NyAyMC45NVE4NC4zNSAyMC45NSA4NC43NCAyMC42M1E4NS4xMyAyMC4zMiA4NS4xMyAxOS44MEw4NS4xMyAxOS44MFE4NS4xMyAxOS4yNCA4NC43MyAxOC45NFE4NC4zNCAxOC42MyA4My4zMSAxOC4zMlE4Mi4yNyAxOC4wMSA4MS42NiAxNy42M0w4MS42NiAxNy42M1E4MC41MCAxNi45MCA4MC41MCAxNS43Mkw4MC41MCAxNS43MlE4MC41MCAxNC42OSA4MS4zNCAxNC4wMlE4Mi4xOCAxMy4zNSA4My41MiAxMy4zNUw4My41MiAxMy4zNVE4NC40MSAxMy4zNSA4NS4xMSAxMy42OFE4NS44MSAxNC4wMSA4Ni4yMSAxNC42MVE4Ni42MCAxNS4yMiA4Ni42MCAxNS45Nkw4Ni42MCAxNS45Nkw4NS4xMyAxNS45NlE4NS4xMyAxNS4yOSA4NC43MSAxNC45MVE4NC4yOSAxNC41NCA4My41MSAxNC41NEw4My41MSAxNC41NFE4Mi43OCAxNC41NCA4Mi4zOCAxNC44NVE4MS45OCAxNS4xNiA4MS45OCAxNS43MUw4MS45OCAxNS43MVE4MS45OCAxNi4xOCA4Mi40MSAxNi41MFE4Mi44NSAxNi44MSA4My44NCAxNy4xMFE4NC44NCAxNy40MCA4NS40NCAxNy43OFE4Ni4wNSAxOC4xNiA4Ni4zMyAxOC42NVE4Ni42MSAxOS4xMyA4Ni42MSAxOS43OUw4Ni42MSAxOS43OVE4Ni42MSAyMC44NiA4NS43OSAyMS40OVE4NC45NyAyMi4xMiA4My41NyAyMi4xMkw4My41NyAyMi4xMlE4Mi42NSAyMi4xMiA4MS44NyAyMS43N1E4MS4xMCAyMS40MyA4MC42NyAyMC44M1E4MC4yMyAyMC4yMiA4MC4yMyAxOS40MloiIGZpbGw9IiMwMDAwMDAiLz48cGF0aCBjbGFzcz0ic3ZnX190ZXh0IiBkPSIiIGZpbGw9IiMwMDAwMDAiIHg9IjExMS4zOSIvPjwvc3ZnPg==)][![forthebadge](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI5Mi4yOCIgaGVpZ2h0PSIzNSIgdmlld0JveD0iMCAwIDkyLjI4IDM1Ij48cmVjdCBjbGFzcz0ic3ZnX19yZWN0IiB4PSIwIiB5PSIwIiB3aWR0aD0iOTIuMjgiIGhlaWdodD0iMzUiIGZpbGw9IiNBMUExQTEiLz48cmVjdCBjbGFzcz0ic3ZnX19yZWN0IiB4PSI5Mi4yOCIgeT0iMCIgd2lkdGg9IjAiIGhlaWdodD0iMzUiIGZpbGw9IiM2RkMyREUiLz48cGF0aCBjbGFzcz0ic3ZnX190ZXh0IiBkPSJNMTUuNzAgMjJMMTQuMjIgMjJMMTQuMjIgMTMuNDdMMTcuMjIgMTMuNDdRMTguNjkgMTMuNDcgMTkuNTAgMTQuMTNRMjAuMzAgMTQuNzkgMjAuMzAgMTYuMDVMMjAuMzAgMTYuMDVRMjAuMzAgMTYuOTAgMTkuODkgMTcuNDhRMTkuNDcgMTguMDYgMTguNzMgMTguMzdMMTguNzMgMTguMzdMMjAuNjUgMjEuOTJMMjAuNjUgMjJMMTkuMDYgMjJMMTcuMzUgMTguNzFMMTUuNzAgMTguNzFMMTUuNzAgMjJaTTE1LjcwIDE0LjY2TDE1LjcwIDE3LjUyTDE3LjIyIDE3LjUyUTE3Ljk3IDE3LjUyIDE4LjM5IDE3LjE1UTE4LjgyIDE2Ljc3IDE4LjgyIDE2LjExTDE4LjgyIDE2LjExUTE4LjgyIDE1LjQzIDE4LjQzIDE1LjA1UTE4LjA0IDE0LjY4IDE3LjI2IDE0LjY2TDE3LjI2IDE0LjY2TDE1LjcwIDE0LjY2Wk0zMC4yNyAyMkwyNC42OSAyMkwyNC42OSAxMy40N0wzMC4yMyAxMy40N0wzMC4yMyAxNC42NkwyNi4xOCAxNC42NkwyNi4xOCAxNy4wMkwyOS42OCAxNy4wMkwyOS42OCAxOC4xOUwyNi4xOCAxOC4xOUwyNi4xOCAyMC44MkwzMC4yNyAyMC44MkwzMC4yNyAyMlpNMzQuMDMgMTkuNDJMMzQuMDMgMTkuNDJMMzUuNTIgMTkuNDJRMzUuNTIgMjAuMTUgMzYuMDAgMjAuNTVRMzYuNDggMjAuOTUgMzcuMzcgMjAuOTVMMzcuMzcgMjAuOTVRMzguMTUgMjAuOTUgMzguNTQgMjAuNjNRMzguOTMgMjAuMzIgMzguOTMgMTkuODBMMzguOTMgMTkuODBRMzguOTMgMTkuMjQgMzguNTMgMTguOTRRMzguMTQgMTguNjMgMzcuMTAgMTguMzJRMzYuMDcgMTguMDEgMzUuNDYgMTcuNjNMMzUuNDYgMTcuNjNRMzQuMzAgMTYuOTAgMzQuMzAgMTUuNzJMMzQuMzAgMTUuNzJRMzQuMzAgMTQuNjkgMzUuMTQgMTQuMDJRMzUuOTggMTMuMzUgMzcuMzIgMTMuMzVMMzcuMzIgMTMuMzVRMzguMjEgMTMuMzUgMzguOTEgMTMuNjhRMzkuNjEgMTQuMDEgNDAuMDAgMTQuNjFRNDAuNDAgMTUuMjIgNDAuNDAgMTUuOTZMNDAuNDAgMTUuOTZMMzguOTMgMTUuOTZRMzguOTMgMTUuMjkgMzguNTEgMTQuOTFRMzguMDkgMTQuNTQgMzcuMzEgMTQuNTRMMzcuMzEgMTQuNTRRMzYuNTggMTQuNTQgMzYuMTggMTQuODVRMzUuNzggMTUuMTYgMzUuNzggMTUuNzFMMzUuNzggMTUuNzFRMzUuNzggMTYuMTggMzYuMjEgMTYuNTBRMzYuNjUgMTYuODEgMzcuNjQgMTcuMTBRMzguNjQgMTcuNDAgMzkuMjQgMTcuNzhRMzkuODUgMTguMTYgNDAuMTMgMTguNjVRNDAuNDEgMTkuMTMgNDAuNDEgMTkuNzlMNDAuNDEgMTkuNzlRNDAuNDEgMjAuODYgMzkuNTkgMjEuNDlRMzguNzcgMjIuMTIgMzcuMzcgMjIuMTJMMzcuMzcgMjIuMTJRMzYuNDUgMjIuMTIgMzUuNjcgMjEuNzdRMzQuODkgMjEuNDMgMzQuNDYgMjAuODNRMzQuMDMgMjAuMjIgMzQuMDMgMTkuNDJaTTQ0LjU2IDE5LjE2TDQ0LjU2IDE5LjE2TDQ0LjU2IDEzLjQ3TDQ2LjA0IDEzLjQ3TDQ2LjA0IDE5LjE4UTQ2LjA0IDIwLjAzIDQ2LjQ3IDIwLjQ4UTQ2LjkxIDIwLjkzIDQ3Ljc1IDIwLjkzTDQ3Ljc1IDIwLjkzUTQ5LjQ2IDIwLjkzIDQ5LjQ2IDE5LjEzTDQ5LjQ2IDE5LjEzTDQ5LjQ2IDEzLjQ3TDUwLjk0IDEzLjQ3TDUwLjk0IDE5LjE3UTUwLjk0IDIwLjUzIDUwLjA3IDIxLjMyUTQ5LjIwIDIyLjEyIDQ3Ljc1IDIyLjEyTDQ3Ljc1IDIyLjEyUTQ2LjI5IDIyLjEyIDQ1LjQyIDIxLjMzUTQ0LjU2IDIwLjU1IDQ0LjU2IDE5LjE2Wk02MC44NiAyMkw1NS41MSAyMkw1NS41MSAxMy40N0w1Ni45OSAxMy40N0w1Ni45OSAyMC44Mkw2MC44NiAyMC44Mkw2MC44NiAyMlpNNjYuNjcgMTQuNjZMNjQuMDMgMTQuNjZMNjQuMDMgMTMuNDdMNzAuODAgMTMuNDdMNzAuODAgMTQuNjZMNjguMTQgMTQuNjZMNjguMTQgMjJMNjYuNjcgMjJMNjYuNjcgMTQuNjZaTTc0LjEyIDE5LjQyTDc0LjEyIDE5LjQyTDc1LjYxIDE5LjQyUTc1LjYxIDIwLjE1IDc2LjA5IDIwLjU1UTc2LjU3IDIwLjk1IDc3LjQ2IDIwLjk1TDc3LjQ2IDIwLjk1UTc4LjI0IDIwLjk1IDc4LjYzIDIwLjYzUTc5LjAyIDIwLjMyIDc5LjAyIDE5LjgwTDc5LjAyIDE5LjgwUTc5LjAyIDE5LjI0IDc4LjYyIDE4Ljk0UTc4LjIyIDE4LjYzIDc3LjE5IDE4LjMyUTc2LjE2IDE4LjAxIDc1LjU1IDE3LjYzTDc1LjU1IDE3LjYzUTc0LjM5IDE2LjkwIDc0LjM5IDE1LjcyTDc0LjM5IDE1LjcyUTc0LjM5IDE0LjY5IDc1LjIzIDE0LjAyUTc2LjA3IDEzLjM1IDc3LjQxIDEzLjM1TDc3LjQxIDEzLjM1UTc4LjMwIDEzLjM1IDc5LjAwIDEzLjY4UTc5LjcwIDE0LjAxIDgwLjA5IDE0LjYxUTgwLjQ5IDE1LjIyIDgwLjQ5IDE1Ljk2TDgwLjQ5IDE1Ljk2TDc5LjAyIDE1Ljk2UTc5LjAyIDE1LjI5IDc4LjYwIDE0LjkxUTc4LjE4IDE0LjU0IDc3LjQwIDE0LjU0TDc3LjQwIDE0LjU0UTc2LjY3IDE0LjU0IDc2LjI3IDE0Ljg1UTc1Ljg3IDE1LjE2IDc1Ljg3IDE1LjcxTDc1Ljg3IDE1LjcxUTc1Ljg3IDE2LjE4IDc2LjMwIDE2LjUwUTc2Ljc0IDE2LjgxIDc3LjczIDE3LjEwUTc4LjczIDE3LjQwIDc5LjMzIDE3Ljc4UTc5Ljk0IDE4LjE2IDgwLjIyIDE4LjY1UTgwLjUwIDE5LjEzIDgwLjUwIDE5Ljc5TDgwLjUwIDE5Ljc5UTgwLjUwIDIwLjg2IDc5LjY4IDIxLjQ5UTc4Ljg2IDIyLjEyIDc3LjQ2IDIyLjEyTDc3LjQ2IDIyLjEyUTc2LjU0IDIyLjEyIDc1Ljc2IDIxLjc3UTc0Ljk4IDIxLjQzIDc0LjU1IDIwLjgzUTc0LjEyIDIwLjIyIDc0LjEyIDE5LjQyWiIgZmlsbD0iIzAwMDAwMCIvPjxwYXRoIGNsYXNzPSJzdmdfX3RleHQiIGQ9IiIgZmlsbD0iIzAwMDAwMCIgeD0iMTA1LjI4Ii8+PC9zdmc+)](https://novelmovementcph.streamlit.app/Results_%F0%9F%93%8A)
[![forthebadge](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMjUuNjMiIGhlaWdodD0iMzUiIHZpZXdCb3g9IjAgMCAxMjUuNjMgMzUiPjxyZWN0IGNsYXNzPSJzdmdfX3JlY3QiIHg9IjAiIHk9IjAiIHdpZHRoPSIxMjUuNjMiIGhlaWdodD0iMzUiIGZpbGw9IiNBMUExQTEiLz48cmVjdCBjbGFzcz0ic3ZnX19yZWN0IiB4PSIxMjUuNjMiIHk9IjAiIHdpZHRoPSIwIiBoZWlnaHQ9IjM1IiBmaWxsPSIjNkZDMkRFIi8+PHBhdGggY2xhc3M9InN2Z19fdGV4dCIgZD0iTTEzLjk1IDE4LjE5TDEzLjk1IDE4LjE5TDEzLjk1IDE3LjM5UTEzLjk1IDE2LjE5IDE0LjM4IDE1LjI3UTE0LjgwIDE0LjM1IDE1LjYwIDEzLjg1UTE2LjQwIDEzLjM1IDE3LjQ1IDEzLjM1TDE3LjQ1IDEzLjM1UTE4Ljg2IDEzLjM1IDE5LjczIDE0LjEyUTIwLjU5IDE0Ljg5IDIwLjczIDE2LjI5TDIwLjczIDE2LjI5TDE5LjI1IDE2LjI5UTE5LjE0IDE1LjM3IDE4LjcxIDE0Ljk2UTE4LjI4IDE0LjU1IDE3LjQ1IDE0LjU1TDE3LjQ1IDE0LjU1UTE2LjQ4IDE0LjU1IDE1Ljk3IDE1LjI2UTE1LjQ1IDE1Ljk2IDE1LjQ0IDE3LjMzTDE1LjQ0IDE3LjMzTDE1LjQ0IDE4LjA5UTE1LjQ0IDE5LjQ3IDE1LjkzIDIwLjIwUTE2LjQzIDIwLjkyIDE3LjM4IDIwLjkyTDE3LjM4IDIwLjkyUTE4LjI1IDIwLjkyIDE4LjY5IDIwLjUzUTE5LjEzIDIwLjE0IDE5LjI1IDE5LjIyTDE5LjI1IDE5LjIyTDIwLjczIDE5LjIyUTIwLjYwIDIwLjU5IDE5LjcyIDIxLjM1UTE4Ljg0IDIyLjEyIDE3LjM4IDIyLjEyTDE3LjM4IDIyLjEyUTE2LjM2IDIyLjEyIDE1LjU5IDIxLjYzUTE0LjgxIDIxLjE1IDE0LjM5IDIwLjI2UTEzLjk3IDE5LjM3IDEzLjk1IDE4LjE5Wk0yNC43NyAxOC4wMEwyNC43NyAxOC4wMEwyNC43NyAxNy41MlEyNC43NyAxNi4yOCAyNS4yMSAxNS4zMlEyNS42NSAxNC4zNyAyNi40NiAxMy44NlEyNy4yNyAxMy4zNSAyOC4zMSAxMy4zNVEyOS4zNSAxMy4zNSAzMC4xNiAxMy44NVEzMC45NiAxNC4zNSAzMS40MCAxNS4yOVEzMS44NCAxNi4yMyAzMS44NSAxNy40OEwzMS44NSAxNy40OEwzMS44NSAxNy45NlEzMS44NSAxOS4yMSAzMS40MSAyMC4xNlEzMC45OCAyMS4xMCAzMC4xOCAyMS42MVEyOS4zNyAyMi4xMiAyOC4zMiAyMi4xMkwyOC4zMiAyMi4xMlEyNy4yOCAyMi4xMiAyNi40NyAyMS42MVEyNS42NiAyMS4xMCAyNS4yMiAyMC4xN1EyNC43OCAxOS4yMyAyNC43NyAxOC4wMFpNMjYuMjUgMTcuNDZMMjYuMjUgMTcuOTZRMjYuMjUgMTkuMzYgMjYuODAgMjAuMTNRMjcuMzUgMjAuOTAgMjguMzIgMjAuOTBMMjguMzIgMjAuOTBRMjkuMzEgMjAuOTAgMjkuODQgMjAuMTVRMzAuMzcgMTkuNDAgMzAuMzcgMTcuOTZMMzAuMzcgMTcuOTZMMzAuMzcgMTcuNTFRMzAuMzcgMTYuMDkgMjkuODMgMTUuMzRRMjkuMjkgMTQuNTggMjguMzEgMTQuNThMMjguMzEgMTQuNThRMjcuMzUgMTQuNTggMjYuODEgMTUuMzNRMjYuMjYgMTYuMDkgMjYuMjUgMTcuNDZMMjYuMjUgMTcuNDZaTTM3LjgwIDIyTDM2LjMxIDIyTDM2LjMxIDEzLjQ3TDM3LjgwIDEzLjQ3TDQxLjYxIDE5LjU0TDQxLjYxIDEzLjQ3TDQzLjA4IDEzLjQ3TDQzLjA4IDIyTDQxLjYwIDIyTDM3LjgwIDE1Ljk1TDM3LjgwIDIyWk00Ny41NSAxOC4xOUw0Ny41NSAxOC4xOUw0Ny41NSAxNy4zOVE0Ny41NSAxNi4xOSA0Ny45OCAxNS4yN1E0OC40MSAxNC4zNSA0OS4yMSAxMy44NVE1MC4wMSAxMy4zNSA1MS4wNiAxMy4zNUw1MS4wNiAxMy4zNVE1Mi40NyAxMy4zNSA1My4zMyAxNC4xMlE1NC4xOSAxNC44OSA1NC4zMyAxNi4yOUw1NC4zMyAxNi4yOUw1Mi44NSAxNi4yOVE1Mi43NSAxNS4zNyA1Mi4zMiAxNC45NlE1MS44OSAxNC41NSA1MS4wNiAxNC41NUw1MS4wNiAxNC41NVE1MC4wOSAxNC41NSA0OS41NyAxNS4yNlE0OS4wNSAxNS45NiA0OS4wNCAxNy4zM0w0OS4wNCAxNy4zM0w0OS4wNCAxOC4wOVE0OS4wNCAxOS40NyA0OS41MyAyMC4yMFE1MC4wMyAyMC45MiA1MC45OCAyMC45Mkw1MC45OCAyMC45MlE1MS44NiAyMC45MiA1Mi4zMCAyMC41M1E1Mi43NCAyMC4xNCA1Mi44NSAxOS4yMkw1Mi44NSAxOS4yMkw1NC4zMyAxOS4yMlE1NC4yMCAyMC41OSA1My4zMiAyMS4zNVE1Mi40NCAyMi4xMiA1MC45OCAyMi4xMkw1MC45OCAyMi4xMlE0OS45NyAyMi4xMiA0OS4xOSAyMS42M1E0OC40MSAyMS4xNSA0Ny45OSAyMC4yNlE0Ny41NyAxOS4zNyA0Ny41NSAxOC4xOVpNNjQuMDAgMjJMNTguNjQgMjJMNTguNjQgMTMuNDdMNjAuMTMgMTMuNDdMNjAuMTMgMjAuODJMNjQuMDAgMjAuODJMNjQuMDAgMjJaTTY3Ljk5IDE5LjE2TDY3Ljk5IDE5LjE2TDY3Ljk5IDEzLjQ3TDY5LjQ3IDEzLjQ3TDY5LjQ3IDE5LjE4UTY5LjQ3IDIwLjAzIDY5LjkwIDIwLjQ4UTcwLjMzIDIwLjkzIDcxLjE4IDIwLjkzTDcxLjE4IDIwLjkzUTcyLjg5IDIwLjkzIDcyLjg5IDE5LjEzTDcyLjg5IDE5LjEzTDcyLjg5IDEzLjQ3TDc0LjM2IDEzLjQ3TDc0LjM2IDE5LjE3UTc0LjM2IDIwLjUzIDczLjQ5IDIxLjMyUTcyLjYyIDIyLjEyIDcxLjE4IDIyLjEyTDcxLjE4IDIyLjEyUTY5LjcxIDIyLjEyIDY4Ljg1IDIxLjMzUTY3Ljk5IDIwLjU1IDY3Ljk5IDE5LjE2Wk03OC41MCAxOS40Mkw3OC41MCAxOS40Mkw3OS45OCAxOS40MlE3OS45OCAyMC4xNSA4MC40NiAyMC41NVE4MC45NCAyMC45NSA4MS44NCAyMC45NUw4MS44NCAyMC45NVE4Mi42MSAyMC45NSA4My4wMCAyMC42M1E4My4zOSAyMC4zMiA4My4zOSAxOS44MEw4My4zOSAxOS44MFE4My4zOSAxOS4yNCA4My4wMCAxOC45NFE4Mi42MCAxOC42MyA4MS41NyAxOC4zMlE4MC41NCAxOC4wMSA3OS45MyAxNy42M0w3OS45MyAxNy42M1E3OC43NiAxNi45MCA3OC43NiAxNS43Mkw3OC43NiAxNS43MlE3OC43NiAxNC42OSA3OS42MCAxNC4wMlE4MC40NSAxMy4zNSA4MS43OSAxMy4zNUw4MS43OSAxMy4zNVE4Mi42OCAxMy4zNSA4My4zOCAxMy42OFE4NC4wNyAxNC4wMSA4NC40NyAxNC42MVE4NC44NyAxNS4yMiA4NC44NyAxNS45Nkw4NC44NyAxNS45Nkw4My4zOSAxNS45NlE4My4zOSAxNS4yOSA4Mi45NyAxNC45MVE4Mi41NiAxNC41NCA4MS43OCAxNC41NEw4MS43OCAxNC41NFE4MS4wNSAxNC41NCA4MC42NSAxNC44NVE4MC4yNSAxNS4xNiA4MC4yNSAxNS43MUw4MC4yNSAxNS43MVE4MC4yNSAxNi4xOCA4MC42OCAxNi41MFE4MS4xMSAxNi44MSA4Mi4xMSAxNy4xMFE4My4xMSAxNy40MCA4My43MSAxNy43OFE4NC4zMSAxOC4xNiA4NC41OSAxOC42NVE4NC44OCAxOS4xMyA4NC44OCAxOS43OUw4NC44OCAxOS43OVE4NC44OCAyMC44NiA4NC4wNiAyMS40OVE4My4yNCAyMi4xMiA4MS44NCAyMi4xMkw4MS44NCAyMi4xMlE4MC45MSAyMi4xMiA4MC4xNCAyMS43N1E3OS4zNiAyMS40MyA3OC45MyAyMC44M1E3OC41MCAyMC4yMiA3OC41MCAxOS40MlpNOTAuNzMgMjJMODkuMjUgMjJMODkuMjUgMTMuNDdMOTAuNzMgMTMuNDdMOTAuNzMgMjJaTTk1LjI3IDE4LjAwTDk1LjI3IDE4LjAwTDk1LjI3IDE3LjUyUTk1LjI3IDE2LjI4IDk1LjcxIDE1LjMyUTk2LjE1IDE0LjM3IDk2Ljk2IDEzLjg2UTk3Ljc3IDEzLjM1IDk4LjgxIDEzLjM1UTk5Ljg1IDEzLjM1IDEwMC42NiAxMy44NVExMDEuNDYgMTQuMzUgMTAxLjkwIDE1LjI5UTEwMi4zNCAxNi4yMyAxMDIuMzUgMTcuNDhMMTAyLjM1IDE3LjQ4TDEwMi4zNSAxNy45NlExMDIuMzUgMTkuMjEgMTAxLjkxIDIwLjE2UTEwMS40OCAyMS4xMCAxMDAuNjggMjEuNjFROTkuODcgMjIuMTIgOTguODIgMjIuMTJMOTguODIgMjIuMTJROTcuNzggMjIuMTIgOTYuOTcgMjEuNjFROTYuMTYgMjEuMTAgOTUuNzIgMjAuMTdROTUuMjggMTkuMjMgOTUuMjcgMTguMDBaTTk2Ljc1IDE3LjQ2TDk2Ljc1IDE3Ljk2UTk2Ljc1IDE5LjM2IDk3LjMwIDIwLjEzUTk3Ljg1IDIwLjkwIDk4LjgyIDIwLjkwTDk4LjgyIDIwLjkwUTk5LjgxIDIwLjkwIDEwMC4zNCAyMC4xNVExMDAuODcgMTkuNDAgMTAwLjg3IDE3Ljk2TDEwMC44NyAxNy45NkwxMDAuODcgMTcuNTFRMTAwLjg3IDE2LjA5IDEwMC4zMyAxNS4zNFE5OS43OSAxNC41OCA5OC44MSAxNC41OEw5OC44MSAxNC41OFE5Ny44NSAxNC41OCA5Ny4zMSAxNS4zM1E5Ni43NiAxNi4wOSA5Ni43NSAxNy40Nkw5Ni43NSAxNy40NlpNMTA4LjMwIDIyTDEwNi44MSAyMkwxMDYuODEgMTMuNDdMMTA4LjMwIDEzLjQ3TDExMi4xMSAxOS41NEwxMTIuMTEgMTMuNDdMMTEzLjU4IDEzLjQ3TDExMy41OCAyMkwxMTIuMTAgMjJMMTA4LjMwIDE1Ljk1TDEwOC4zMCAyMloiIGZpbGw9IiMwMDAwMDAiLz48cGF0aCBjbGFzcz0ic3ZnX190ZXh0IiBkPSIiIGZpbGw9IiMwMDAwMDAiIHg9IjEzOC42MyIvPjwvc3ZnPg==)](https://novelmovementcph.streamlit.app/Conclusion_%F0%9F%92%8A)
"""
st.title("Methods")
topside1, topside2 = st.columns([1,1])
topside1.markdown(
"""
Ten adults (M = 62.0 years; SD = 7.6) 
with incomplete cervical SCI performed UE tasks from the CUE-T while wering a wrist-worn wearable device (ActiGraph GT9X Link) on their dominant UE.

The wearable device captured acceleration data in the x, y, and z planes at 100 hertz sampling frequency. Assessments were performed in an inpatient rehabilitation facility for individuals with acute injury (n = 5) and community settings for Veterans with chronic injury (n = 5) at baseline and follow-up, approximately four weeks later.

""", unsafe_allow_html=True)

topside2.video('https://www.youtube.com/watch?v=6VEuGwl6hnc')

"""
Acceleration features (e.g., mean, min, max) were extracted using a sliding window technique (1-second window, 0.5-second step). 
"""



acc = [feat for feat in data.columns if feat.startswith('Acc')]
res = [feat for feat in data.columns if feat.startswith('Res')]
with st.expander("Features Used for Model Training"):
    st.multiselect("Features Used for Model Training", 
                options = acc + res, 
                label_visibility='hidden')

#topside2.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRySanzSa_A8VtpgIujOpP6WNUSG2hvLCEmLA&usqp=CAU')
"""
The novelty detection model (local outlier factor) [8] was trained with baseline CUE-T acceleration features for hand and arm movements. 

"""
image = Image.open('D:/PHIRE/CPH/pages/train.png')
with st.expander("Training Procedures"):
    st.image(image)

"""
The model was then applied to post-CUE-T acceleration features of hand and arm movements. A simple linear regression was used to assess the relationship between the mean novel UE movement pattern score in the post-test CUE-T to the overall post-test CUE-T score across participants for the hand and arm.
"""
image2 = Image.open('D:/PHIRE/CPH/pages/test.png')
with st.expander("Application Procedures"):
    st.image(image2, caption = 'xx')



"""
[![forthebadge](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI0MDEuMDMiIGhlaWdodD0iMzUiIHZpZXdCb3g9IjAgMCA0MDEuMDMgMzUiPjxyZWN0IGNsYXNzPSJzdmdfX3JlY3QiIHg9IjAiIHk9IjAiIHdpZHRoPSI5NC4yOCIgaGVpZ2h0PSIzNSIgZmlsbD0iIzNDOUFENSIvPjxyZWN0IGNsYXNzPSJzdmdfX3JlY3QiIHg9IjkyLjI4IiB5PSIwIiB3aWR0aD0iMzA4Ljc1IiBoZWlnaHQ9IjM1IiBmaWxsPSIjNkZDMkRFIi8+PHBhdGggY2xhc3M9InN2Z19fdGV4dCIgZD0iTTE1LjcwIDIyTDE0LjIyIDIyTDE0LjIyIDEzLjQ3TDE3LjIyIDEzLjQ3UTE4LjY5IDEzLjQ3IDE5LjUwIDE0LjEzUTIwLjMwIDE0Ljc5IDIwLjMwIDE2LjA1TDIwLjMwIDE2LjA1UTIwLjMwIDE2LjkwIDE5Ljg5IDE3LjQ4UTE5LjQ3IDE4LjA2IDE4LjczIDE4LjM3TDE4LjczIDE4LjM3TDIwLjY1IDIxLjkyTDIwLjY1IDIyTDE5LjA2IDIyTDE3LjM1IDE4LjcxTDE1LjcwIDE4LjcxTDE1LjcwIDIyWk0xNS43MCAxNC42NkwxNS43MCAxNy41MkwxNy4yMiAxNy41MlExNy45NyAxNy41MiAxOC4zOSAxNy4xNVExOC44MiAxNi43NyAxOC44MiAxNi4xMUwxOC44MiAxNi4xMVExOC44MiAxNS40MyAxOC40MyAxNS4wNVExOC4wNCAxNC42OCAxNy4yNiAxNC42NkwxNy4yNiAxNC42NkwxNS43MCAxNC42NlpNMzAuMjcgMjJMMjQuNjkgMjJMMjQuNjkgMTMuNDdMMzAuMjMgMTMuNDdMMzAuMjMgMTQuNjZMMjYuMTggMTQuNjZMMjYuMTggMTcuMDJMMjkuNjggMTcuMDJMMjkuNjggMTguMTlMMjYuMTggMTguMTlMMjYuMTggMjAuODJMMzAuMjcgMjAuODJMMzAuMjcgMjJaTTM0LjAzIDE5LjQyTDM0LjAzIDE5LjQyTDM1LjUyIDE5LjQyUTM1LjUyIDIwLjE1IDM2LjAwIDIwLjU1UTM2LjQ4IDIwLjk1IDM3LjM3IDIwLjk1TDM3LjM3IDIwLjk1UTM4LjE1IDIwLjk1IDM4LjU0IDIwLjYzUTM4LjkzIDIwLjMyIDM4LjkzIDE5LjgwTDM4LjkzIDE5LjgwUTM4LjkzIDE5LjI0IDM4LjUzIDE4Ljk0UTM4LjE0IDE4LjYzIDM3LjEwIDE4LjMyUTM2LjA3IDE4LjAxIDM1LjQ2IDE3LjYzTDM1LjQ2IDE3LjYzUTM0LjMwIDE2LjkwIDM0LjMwIDE1LjcyTDM0LjMwIDE1LjcyUTM0LjMwIDE0LjY5IDM1LjE0IDE0LjAyUTM1Ljk4IDEzLjM1IDM3LjMyIDEzLjM1TDM3LjMyIDEzLjM1UTM4LjIxIDEzLjM1IDM4LjkxIDEzLjY4UTM5LjYxIDE0LjAxIDQwLjAwIDE0LjYxUTQwLjQwIDE1LjIyIDQwLjQwIDE1Ljk2TDQwLjQwIDE1Ljk2TDM4LjkzIDE1Ljk2UTM4LjkzIDE1LjI5IDM4LjUxIDE0LjkxUTM4LjA5IDE0LjU0IDM3LjMxIDE0LjU0TDM3LjMxIDE0LjU0UTM2LjU4IDE0LjU0IDM2LjE4IDE0Ljg1UTM1Ljc4IDE1LjE2IDM1Ljc4IDE1LjcxTDM1Ljc4IDE1LjcxUTM1Ljc4IDE2LjE4IDM2LjIxIDE2LjUwUTM2LjY1IDE2LjgxIDM3LjY0IDE3LjEwUTM4LjY0IDE3LjQwIDM5LjI0IDE3Ljc4UTM5Ljg1IDE4LjE2IDQwLjEzIDE4LjY1UTQwLjQxIDE5LjEzIDQwLjQxIDE5Ljc5TDQwLjQxIDE5Ljc5UTQwLjQxIDIwLjg2IDM5LjU5IDIxLjQ5UTM4Ljc3IDIyLjEyIDM3LjM3IDIyLjEyTDM3LjM3IDIyLjEyUTM2LjQ1IDIyLjEyIDM1LjY3IDIxLjc3UTM0Ljg5IDIxLjQzIDM0LjQ2IDIwLjgzUTM0LjAzIDIwLjIyIDM0LjAzIDE5LjQyWk00NC41NiAxOS4xNkw0NC41NiAxOS4xNkw0NC41NiAxMy40N0w0Ni4wNCAxMy40N0w0Ni4wNCAxOS4xOFE0Ni4wNCAyMC4wMyA0Ni40NyAyMC40OFE0Ni45MSAyMC45MyA0Ny43NSAyMC45M0w0Ny43NSAyMC45M1E0OS40NiAyMC45MyA0OS40NiAxOS4xM0w0OS40NiAxOS4xM0w0OS40NiAxMy40N0w1MC45NCAxMy40N0w1MC45NCAxOS4xN1E1MC45NCAyMC41MyA1MC4wNyAyMS4zMlE0OS4yMCAyMi4xMiA0Ny43NSAyMi4xMkw0Ny43NSAyMi4xMlE0Ni4yOSAyMi4xMiA0NS40MiAyMS4zM1E0NC41NiAyMC41NSA0NC41NiAxOS4xNlpNNjAuODYgMjJMNTUuNTEgMjJMNTUuNTEgMTMuNDdMNTYuOTkgMTMuNDdMNTYuOTkgMjAuODJMNjAuODYgMjAuODJMNjAuODYgMjJaTTY2LjY3IDE0LjY2TDY0LjAzIDE0LjY2TDY0LjAzIDEzLjQ3TDcwLjgwIDEzLjQ3TDcwLjgwIDE0LjY2TDY4LjE0IDE0LjY2TDY4LjE0IDIyTDY2LjY3IDIyTDY2LjY3IDE0LjY2Wk03NC4xMiAxOS40Mkw3NC4xMiAxOS40Mkw3NS42MSAxOS40MlE3NS42MSAyMC4xNSA3Ni4wOSAyMC41NVE3Ni41NyAyMC45NSA3Ny40NiAyMC45NUw3Ny40NiAyMC45NVE3OC4yNCAyMC45NSA3OC42MyAyMC42M1E3OS4wMiAyMC4zMiA3OS4wMiAxOS44MEw3OS4wMiAxOS44MFE3OS4wMiAxOS4yNCA3OC42MiAxOC45NFE3OC4yMiAxOC42MyA3Ny4xOSAxOC4zMlE3Ni4xNiAxOC4wMSA3NS41NSAxNy42M0w3NS41NSAxNy42M1E3NC4zOSAxNi45MCA3NC4zOSAxNS43Mkw3NC4zOSAxNS43MlE3NC4zOSAxNC42OSA3NS4yMyAxNC4wMlE3Ni4wNyAxMy4zNSA3Ny40MSAxMy4zNUw3Ny40MSAxMy4zNVE3OC4zMCAxMy4zNSA3OS4wMCAxMy42OFE3OS43MCAxNC4wMSA4MC4wOSAxNC42MVE4MC40OSAxNS4yMiA4MC40OSAxNS45Nkw4MC40OSAxNS45Nkw3OS4wMiAxNS45NlE3OS4wMiAxNS4yOSA3OC42MCAxNC45MVE3OC4xOCAxNC41NCA3Ny40MCAxNC41NEw3Ny40MCAxNC41NFE3Ni42NyAxNC41NCA3Ni4yNyAxNC44NVE3NS44NyAxNS4xNiA3NS44NyAxNS43MUw3NS44NyAxNS43MVE3NS44NyAxNi4xOCA3Ni4zMCAxNi41MFE3Ni43NCAxNi44MSA3Ny43MyAxNy4xMFE3OC43MyAxNy40MCA3OS4zMyAxNy43OFE3OS45NCAxOC4xNiA4MC4yMiAxOC42NVE4MC41MCAxOS4xMyA4MC41MCAxOS43OUw4MC41MCAxOS43OVE4MC41MCAyMC44NiA3OS42OCAyMS40OVE3OC44NiAyMi4xMiA3Ny40NiAyMi4xMkw3Ny40NiAyMi4xMlE3Ni41NCAyMi4xMiA3NS43NiAyMS43N1E3NC45OCAyMS40MyA3NC41NSAyMC44M1E3NC4xMiAyMC4yMiA3NC4xMiAxOS40MloiIGZpbGw9IiMwMDAwMDAiLz48cGF0aCBjbGFzcz0ic3ZnX190ZXh0IiBkPSJNMTA5LjcxIDE5LjQ2TDEwNi4yMCAxOS40NkwxMDYuMjAgMTcuNzFMMTA5LjcxIDE3LjcxTDEwOS43MSAxOS40NlpNMTE3Ljg1IDE5LjQ2TDExNC4zNCAxOS40NkwxMTQuMzQgMTcuNzFMMTE3Ljg1IDE3LjcxTDExNy44NSAxOS40NlpNMTI1Ljk5IDE5LjQ2TDEyMi40OCAxOS40NkwxMjIuNDggMTcuNzFMMTI1Ljk5IDE3LjcxTDEyNS45OSAxOS40NlpNMTM0LjEyIDE5LjQ2TDEzMC42MiAxOS40NkwxMzAuNjIgMTcuNzFMMTM0LjEyIDE3LjcxTDEzNC4xMiAxOS40NlpNMTQyLjI2IDE5LjQ2TDEzOC43NiAxOS40NkwxMzguNzYgMTcuNzFMMTQyLjI2IDE3LjcxTDE0Mi4yNiAxOS40NlpNMTUwLjQwIDE5LjQ2TDE0Ni45MCAxOS40NkwxNDYuOTAgMTcuNzFMMTUwLjQwIDE3LjcxTDE1MC40MCAxOS40NlpNMTU4LjU0IDE5LjQ2TDE1NS4wNCAxOS40NkwxNTUuMDQgMTcuNzFMMTU4LjU0IDE3LjcxTDE1OC41NCAxOS40NlpNMTY2LjY4IDE5LjQ2TDE2My4xNyAxOS40NkwxNjMuMTcgMTcuNzFMMTY2LjY4IDE3LjcxTDE2Ni42OCAxOS40NlpNMTc0LjgyIDE5LjQ2TDE3MS4zMSAxOS40NkwxNzEuMzEgMTcuNzFMMTc0LjgyIDE3LjcxTDE3NC44MiAxOS40NlpNMTgyLjk2IDE5LjQ2TDE3OS40NSAxOS40NkwxNzkuNDUgMTcuNzFMMTgyLjk2IDE3LjcxTDE4Mi45NiAxOS40NlpNMTkxLjA5IDE5LjQ2TDE4Ny41OSAxOS40NkwxODcuNTkgMTcuNzFMMTkxLjA5IDE3LjcxTDE5MS4wOSAxOS40NlpNMTk5LjIzIDE5LjQ2TDE5NS43MyAxOS40NkwxOTUuNzMgMTcuNzFMMTk5LjIzIDE3LjcxTDE5OS4yMyAxOS40NlpNMjA3LjM3IDE5LjQ2TDIwMy44NyAxOS40NkwyMDMuODcgMTcuNzFMMjA3LjM3IDE3LjcxTDIwNy4zNyAxOS40NlpNMjE1LjUxIDE5LjQ2TDIxMi4wMSAxOS40NkwyMTIuMDEgMTcuNzFMMjE1LjUxIDE3LjcxTDIxNS41MSAxOS40NlpNMjIzLjY1IDE5LjQ2TDIyMC4xNSAxOS40NkwyMjAuMTUgMTcuNzFMMjIzLjY1IDE3LjcxTDIyMy42NSAxOS40NlpNMjMxLjc5IDE5LjQ2TDIyOC4yOCAxOS40NkwyMjguMjggMTcuNzFMMjMxLjc5IDE3LjcxTDIzMS43OSAxOS40NlpNMjM5LjkzIDE5LjQ2TDIzNi40MiAxOS40NkwyMzYuNDIgMTcuNzFMMjM5LjkzIDE3LjcxTDIzOS45MyAxOS40NlpNMjQ4LjA3IDE5LjQ2TDI0NC41NiAxOS40NkwyNDQuNTYgMTcuNzFMMjQ4LjA3IDE3LjcxTDI0OC4wNyAxOS40NlpNMjU2LjIwIDE5LjQ2TDI1Mi43MCAxOS40NkwyNTIuNzAgMTcuNzFMMjU2LjIwIDE3LjcxTDI1Ni4yMCAxOS40NlpNMjY0LjM0IDE5LjQ2TDI2MC44NCAxOS40NkwyNjAuODQgMTcuNzFMMjY0LjM0IDE3LjcxTDI2NC4zNCAxOS40NlpNMjcyLjQ4IDE5LjQ2TDI2OC45OCAxOS40NkwyNjguOTggMTcuNzFMMjcyLjQ4IDE3LjcxTDI3Mi40OCAxOS40NlpNMjgwLjYyIDE5LjQ2TDI3Ny4xMiAxOS40NkwyNzcuMTIgMTcuNzFMMjgwLjYyIDE3LjcxTDI4MC42MiAxOS40NlpNMjg4Ljc2IDE5LjQ2TDI4NS4yNSAxOS40NkwyODUuMjUgMTcuNzFMMjg4Ljc2IDE3LjcxTDI4OC43NiAxOS40NlpNMjk2LjkwIDE5LjQ2TDI5My4zOSAxOS40NkwyOTMuMzkgMTcuNzFMMjk2LjkwIDE3LjcxTDI5Ni45MCAxOS40NlpNMzA1LjA0IDE5LjQ2TDMwMS41MyAxOS40NkwzMDEuNTMgMTcuNzFMMzA1LjA0IDE3LjcxTDMwNS4wNCAxOS40NlpNMzEzLjE3IDE5LjQ2TDMwOS42NyAxOS40NkwzMDkuNjcgMTcuNzFMMzEzLjE3IDE3LjcxTDMxMy4xNyAxOS40NlpNMzIxLjMxIDE5LjQ2TDMxNy44MSAxOS40NkwzMTcuODEgMTcuNzFMMzIxLjMxIDE3LjcxTDMyMS4zMSAxOS40NlpNMzI5LjQ1IDE5LjQ2TDMyNS45NSAxOS40NkwzMjUuOTUgMTcuNzFMMzI5LjQ1IDE3LjcxTDMyOS40NSAxOS40NlpNMzM3LjU5IDE5LjQ2TDMzNC4wOSAxOS40NkwzMzQuMDkgMTcuNzFMMzM3LjU5IDE3LjcxTDMzNy41OSAxOS40NlpNMzQ1LjczIDE5LjQ2TDM0Mi4yMyAxOS40NkwzNDIuMjMgMTcuNzFMMzQ1LjczIDE3LjcxTDM0NS43MyAxOS40NlpNMzUzLjg3IDE5LjQ2TDM1MC4zNiAxOS40NkwzNTAuMzYgMTcuNzFMMzUzLjg3IDE3LjcxTDM1My44NyAxOS40NlpNMzYyLjAxIDE5LjQ2TDM1OC41MCAxOS40NkwzNTguNTAgMTcuNzFMMzYyLjAxIDE3LjcxTDM2Mi4wMSAxOS40NlpNMzcwLjE1IDE5LjQ2TDM2Ni42NCAxOS40NkwzNjYuNjQgMTcuNzFMMzcwLjE1IDE3LjcxTDM3MC4xNSAxOS40NlpNMzc4LjI4IDE5LjQ2TDM3NC43OCAxOS40NkwzNzQuNzggMTcuNzFMMzc4LjI4IDE3LjcxTDM3OC4yOCAxOS40NlpNMzg4Ljk1IDE4LjcyTDM4My4wNCAyMC45MUwzODMuMDQgMTkuMTZMMzg2Ljg3IDE3LjgwTDM4My4wNCAxNi40NUwzODMuMDQgMTQuNjlMMzg4Ljk1IDE2Ljg4TDM4OC45NSAxOC43MloiIGZpbGw9IiMwMDAwMDAiIHg9IjEwNS4yOCIvPjwvc3ZnPg==)](https://novelmovementcph.streamlit.app/Results_%F0%9F%93%8A)
"""
