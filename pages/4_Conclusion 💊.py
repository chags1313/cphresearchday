import streamlit as st
from PIL import Image
"""
[![forthebadge](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNDEuNTUiIGhlaWdodD0iMzUiIHZpZXdCb3g9IjAgMCAxNDEuNTUgMzUiPjxyZWN0IGNsYXNzPSJzdmdfX3JlY3QiIHg9IjAiIHk9IjAiIHdpZHRoPSIxNDEuNTUiIGhlaWdodD0iMzUiIGZpbGw9IiNBMUExQTEiLz48cmVjdCBjbGFzcz0ic3ZnX19yZWN0IiB4PSIxNDEuNTUiIHk9IjAiIHdpZHRoPSIwIiBoZWlnaHQ9IjM1IiBmaWxsPSIjNkZDMkRFIi8+PHBhdGggY2xhc3M9InN2Z19fdGV4dCIgZD0iTTE1Ljc4IDIyTDE0LjMxIDIyTDE0LjMxIDEzLjQ3TDE1Ljc4IDEzLjQ3TDE1Ljc4IDIyWk0yMi4wNyAyMkwyMC41OSAyMkwyMC41OSAxMy40N0wyMi4wNyAxMy40N0wyNS44OSAxOS41NEwyNS44OSAxMy40N0wyNy4zNiAxMy40N0wyNy4zNiAyMkwyNS44OCAyMkwyMi4wNyAxNS45NUwyMi4wNyAyMlpNMzMuNzggMTQuNjZMMzEuMTQgMTQuNjZMMzEuMTQgMTMuNDdMMzcuOTEgMTMuNDdMMzcuOTEgMTQuNjZMMzUuMjUgMTQuNjZMMzUuMjUgMjJMMzMuNzggMjJMMzMuNzggMTQuNjZaTTQzLjE1IDIyTDQxLjY3IDIyTDQxLjY3IDEzLjQ3TDQ0LjY3IDEzLjQ3UTQ2LjE0IDEzLjQ3IDQ2Ljk1IDE0LjEzUTQ3Ljc1IDE0Ljc5IDQ3Ljc1IDE2LjA1TDQ3Ljc1IDE2LjA1UTQ3Ljc1IDE2LjkwIDQ3LjM0IDE3LjQ4UTQ2LjkyIDE4LjA2IDQ2LjE5IDE4LjM3TDQ2LjE5IDE4LjM3TDQ4LjEwIDIxLjkyTDQ4LjEwIDIyTDQ2LjUxIDIyTDQ0LjgwIDE4LjcxTDQzLjE1IDE4LjcxTDQzLjE1IDIyWk00My4xNSAxNC42Nkw0My4xNSAxNy41Mkw0NC42NyAxNy41MlE0NS40MiAxNy41MiA0NS44NSAxNy4xNVE0Ni4yNyAxNi43NyA0Ni4yNyAxNi4xMUw0Ni4yNyAxNi4xMVE0Ni4yNyAxNS40MyA0NS44OCAxNS4wNVE0NS40OSAxNC42OCA0NC43MiAxNC42Nkw0NC43MiAxNC42Nkw0My4xNSAxNC42NlpNNTEuODggMTguMDBMNTEuODggMTguMDBMNTEuODggMTcuNTJRNTEuODggMTYuMjggNTIuMzIgMTUuMzJRNTIuNzYgMTQuMzcgNTMuNTcgMTMuODZRNTQuMzcgMTMuMzUgNTUuNDEgMTMuMzVRNTYuNDYgMTMuMzUgNTcuMjYgMTMuODVRNTguMDcgMTQuMzUgNTguNTEgMTUuMjlRNTguOTUgMTYuMjMgNTguOTUgMTcuNDhMNTguOTUgMTcuNDhMNTguOTUgMTcuOTZRNTguOTUgMTkuMjEgNTguNTIgMjAuMTZRNTguMDkgMjEuMTAgNTcuMjggMjEuNjFRNTYuNDggMjIuMTIgNTUuNDMgMjIuMTJMNTUuNDMgMjIuMTJRNTQuMzkgMjIuMTIgNTMuNTggMjEuNjFRNTIuNzcgMjEuMTAgNTIuMzIgMjAuMTdRNTEuODggMTkuMjMgNTEuODggMTguMDBaTTUzLjM2IDE3LjQ2TDUzLjM2IDE3Ljk2UTUzLjM2IDE5LjM2IDUzLjkxIDIwLjEzUTU0LjQ1IDIwLjkwIDU1LjQzIDIwLjkwTDU1LjQzIDIwLjkwUTU2LjQxIDIwLjkwIDU2Ljk0IDIwLjE1UTU3LjQ3IDE5LjQwIDU3LjQ3IDE3Ljk2TDU3LjQ3IDE3Ljk2TDU3LjQ3IDE3LjUxUTU3LjQ3IDE2LjA5IDU2LjkzIDE1LjM0UTU2LjQwIDE0LjU4IDU1LjQxIDE0LjU4TDU1LjQxIDE0LjU4UTU0LjQ1IDE0LjU4IDUzLjkxIDE1LjMzUTUzLjM3IDE2LjA5IDUzLjM2IDE3LjQ2TDUzLjM2IDE3LjQ2Wk02NS44NyAyMkw2My40MiAyMkw2My40MiAxMy40N0w2NS45NCAxMy40N1E2Ny4wNyAxMy40NyA2Ny45NCAxMy45N1E2OC44MiAxNC40OCA2OS4zMCAxNS40MFE2OS43OCAxNi4zMyA2OS43OCAxNy41Mkw2OS43OCAxNy41Mkw2OS43OCAxNy45NVE2OS43OCAxOS4xNiA2OS4zMCAyMC4wOFE2OC44MSAyMS4wMCA2Ny45MiAyMS41MFE2Ny4wMyAyMiA2NS44NyAyMkw2NS44NyAyMlpNNjQuOTAgMTQuNjZMNjQuOTAgMjAuODJMNjUuODcgMjAuODJRNjcuMDMgMjAuODIgNjcuNjYgMjAuMDlRNjguMjggMTkuMzYgNjguMjkgMTcuOTlMNjguMjkgMTcuOTlMNjguMjkgMTcuNTJRNjguMjkgMTYuMTMgNjcuNjkgMTUuNDBRNjcuMDkgMTQuNjYgNjUuOTQgMTQuNjZMNjUuOTQgMTQuNjZMNjQuOTAgMTQuNjZaTTc0LjExIDE5LjE2TDc0LjExIDE5LjE2TDc0LjExIDEzLjQ3TDc1LjU5IDEzLjQ3TDc1LjU5IDE5LjE4UTc1LjU5IDIwLjAzIDc2LjAyIDIwLjQ4UTc2LjQ2IDIwLjkzIDc3LjMwIDIwLjkzTDc3LjMwIDIwLjkzUTc5LjAxIDIwLjkzIDc5LjAxIDE5LjEzTDc5LjAxIDE5LjEzTDc5LjAxIDEzLjQ3TDgwLjQ5IDEzLjQ3TDgwLjQ5IDE5LjE3UTgwLjQ5IDIwLjUzIDc5LjYyIDIxLjMyUTc4Ljc1IDIyLjEyIDc3LjMwIDIyLjEyTDc3LjMwIDIyLjEyUTc1LjgzIDIyLjEyIDc0Ljk3IDIxLjMzUTc0LjExIDIwLjU1IDc0LjExIDE5LjE2Wk04NC43OSAxOC4xOUw4NC43OSAxOC4xOUw4NC43OSAxNy4zOVE4NC43OSAxNi4xOSA4NS4yMiAxNS4yN1E4NS42NCAxNC4zNSA4Ni40NCAxMy44NVE4Ny4yNCAxMy4zNSA4OC4yOSAxMy4zNUw4OC4yOSAxMy4zNVE4OS43MCAxMy4zNSA5MC41NiAxNC4xMlE5MS40MyAxNC44OSA5MS41NyAxNi4yOUw5MS41NyAxNi4yOUw5MC4wOSAxNi4yOVE4OS45OCAxNS4zNyA4OS41NSAxNC45NlE4OS4xMiAxNC41NSA4OC4yOSAxNC41NUw4OC4yOSAxNC41NVE4Ny4zMiAxNC41NSA4Ni44MSAxNS4yNlE4Ni4yOSAxNS45NiA4Ni4yOCAxNy4zM0w4Ni4yOCAxNy4zM0w4Ni4yOCAxOC4wOVE4Ni4yOCAxOS40NyA4Ni43NyAyMC4yMFE4Ny4yNyAyMC45MiA4OC4yMiAyMC45Mkw4OC4yMiAyMC45MlE4OS4wOSAyMC45MiA4OS41MyAyMC41M1E4OS45NyAyMC4xNCA5MC4wOSAxOS4yMkw5MC4wOSAxOS4yMkw5MS41NyAxOS4yMlE5MS40NCAyMC41OSA5MC41NiAyMS4zNVE4OS42OCAyMi4xMiA4OC4yMiAyMi4xMkw4OC4yMiAyMi4xMlE4Ny4yMCAyMi4xMiA4Ni40MyAyMS42M1E4NS42NSAyMS4xNSA4NS4yMyAyMC4yNlE4NC44MSAxOS4zNyA4NC43OSAxOC4xOVpNOTcuNTYgMTQuNjZMOTQuOTIgMTQuNjZMOTQuOTIgMTMuNDdMMTAxLjY5IDEzLjQ3TDEwMS42OSAxNC42Nkw5OS4wMyAxNC42Nkw5OS4wMyAyMkw5Ny41NiAyMkw5Ny41NiAxNC42NlpNMTA3LjAxIDIyTDEwNS41NCAyMkwxMDUuNTQgMTMuNDdMMTA3LjAxIDEzLjQ3TDEwNy4wMSAyMlpNMTExLjU1IDE4LjAwTDExMS41NSAxOC4wMEwxMTEuNTUgMTcuNTJRMTExLjU1IDE2LjI4IDExMi4wMCAxNS4zMlExMTIuNDQgMTQuMzcgMTEzLjI0IDEzLjg2UTExNC4wNSAxMy4zNSAxMTUuMDkgMTMuMzVRMTE2LjE0IDEzLjM1IDExNi45NCAxMy44NVExMTcuNzUgMTQuMzUgMTE4LjE5IDE1LjI5UTExOC42MyAxNi4yMyAxMTguNjMgMTcuNDhMMTE4LjYzIDE3LjQ4TDExOC42MyAxNy45NlExMTguNjMgMTkuMjEgMTE4LjIwIDIwLjE2UTExNy43NiAyMS4xMCAxMTYuOTYgMjEuNjFRMTE2LjE1IDIyLjEyIDExNS4xMCAyMi4xMkwxMTUuMTAgMjIuMTJRMTE0LjA3IDIyLjEyIDExMy4yNiAyMS42MVExMTIuNDQgMjEuMTAgMTEyLjAwIDIwLjE3UTExMS41NiAxOS4yMyAxMTEuNTUgMTguMDBaTTExMy4wNCAxNy40NkwxMTMuMDQgMTcuOTZRMTEzLjA0IDE5LjM2IDExMy41OCAyMC4xM1ExMTQuMTMgMjAuOTAgMTE1LjEwIDIwLjkwTDExNS4xMCAyMC45MFExMTYuMDkgMjAuOTAgMTE2LjYyIDIwLjE1UTExNy4xNSAxOS40MCAxMTcuMTUgMTcuOTZMMTE3LjE1IDE3Ljk2TDExNy4xNSAxNy41MVExMTcuMTUgMTYuMDkgMTE2LjYxIDE1LjM0UTExNi4wOCAxNC41OCAxMTUuMDkgMTQuNThMMTE1LjA5IDE0LjU4UTExNC4xMyAxNC41OCAxMTMuNTkgMTUuMzNRMTEzLjA1IDE2LjA5IDExMy4wNCAxNy40NkwxMTMuMDQgMTcuNDZaTTEyNC41OCAyMkwxMjMuMTAgMjJMMTIzLjEwIDEzLjQ3TDEyNC41OCAxMy40N0wxMjguMzkgMTkuNTRMMTI4LjM5IDEzLjQ3TDEyOS44NiAxMy40N0wxMjkuODYgMjJMMTI4LjM4IDIyTDEyNC41OCAxNS45NUwxMjQuNTggMjJaIiBmaWxsPSIjMDAwMDAwIi8+PHBhdGggY2xhc3M9InN2Z19fdGV4dCIgZD0iIiBmaWxsPSIjMDAwMDAwIiB4PSIxNTQuNTUiLz48L3N2Zz4=)](https://novelmovementcph.streamlit.app/Introduction_%F0%9F%8F%A0)
[![forthebadge](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI5OC4zOSIgaGVpZ2h0PSIzNSIgdmlld0JveD0iMCAwIDk4LjM5IDM1Ij48cmVjdCBjbGFzcz0ic3ZnX19yZWN0IiB4PSIwIiB5PSIwIiB3aWR0aD0iOTguMzkiIGhlaWdodD0iMzUiIGZpbGw9IiNBMUExQTEiLz48cmVjdCBjbGFzcz0ic3ZnX19yZWN0IiB4PSI5OC4zOSIgeT0iMCIgd2lkdGg9IjAiIGhlaWdodD0iMzUiIGZpbGw9IiM2RkMyREUiLz48cGF0aCBjbGFzcz0ic3ZnX190ZXh0IiBkPSJNMTUuNjkgMjJMMTQuMjIgMjJMMTQuMjIgMTMuNDdMMTYuMTQgMTMuNDdMMTguNjAgMjAuMDFMMjEuMDYgMTMuNDdMMjIuOTcgMTMuNDdMMjIuOTcgMjJMMjEuNDkgMjJMMjEuNDkgMTkuMTlMMjEuNjQgMTUuNDNMMTkuMTIgMjJMMTguMDYgMjJMMTUuNTUgMTUuNDNMMTUuNjkgMTkuMTlMMTUuNjkgMjJaTTMzLjI5IDIyTDI3LjcxIDIyTDI3LjcxIDEzLjQ3TDMzLjI1IDEzLjQ3TDMzLjI1IDE0LjY2TDI5LjE5IDE0LjY2TDI5LjE5IDE3LjAyTDMyLjcwIDE3LjAyTDMyLjcwIDE4LjE5TDI5LjE5IDE4LjE5TDI5LjE5IDIwLjgyTDMzLjI5IDIwLjgyTDMzLjI5IDIyWk0zOS4xNyAxNC42NkwzNi41MyAxNC42NkwzNi41MyAxMy40N0w0My4zMCAxMy40N0w0My4zMCAxNC42Nkw0MC42NCAxNC42Nkw0MC42NCAyMkwzOS4xNyAyMkwzOS4xNyAxNC42NlpNNDguNTQgMjJMNDcuMDUgMjJMNDcuMDUgMTMuNDdMNDguNTQgMTMuNDdMNDguNTQgMTcuMDJMNTIuMzUgMTcuMDJMNTIuMzUgMTMuNDdMNTMuODMgMTMuNDdMNTMuODMgMjJMNTIuMzUgMjJMNTIuMzUgMTguMjFMNDguNTQgMTguMjFMNDguNTQgMjJaTTU4LjMwIDE4LjAwTDU4LjMwIDE4LjAwTDU4LjMwIDE3LjUyUTU4LjMwIDE2LjI4IDU4Ljc0IDE1LjMyUTU5LjE4IDE0LjM3IDU5Ljk5IDEzLjg2UTYwLjc5IDEzLjM1IDYxLjg0IDEzLjM1UTYyLjg4IDEzLjM1IDYzLjY4IDEzLjg1UTY0LjQ5IDE0LjM1IDY0LjkzIDE1LjI5UTY1LjM3IDE2LjIzIDY1LjM4IDE3LjQ4TDY1LjM4IDE3LjQ4TDY1LjM4IDE3Ljk2UTY1LjM4IDE5LjIxIDY0Ljk0IDIwLjE2UTY0LjUxIDIxLjEwIDYzLjcwIDIxLjYxUTYyLjkwIDIyLjEyIDYxLjg1IDIyLjEyTDYxLjg1IDIyLjEyUTYwLjgxIDIyLjEyIDYwLjAwIDIxLjYxUTU5LjE5IDIxLjEwIDU4Ljc1IDIwLjE3UTU4LjMwIDE5LjIzIDU4LjMwIDE4LjAwWk01OS43OCAxNy40Nkw1OS43OCAxNy45NlE1OS43OCAxOS4zNiA2MC4zMyAyMC4xM1E2MC44OCAyMC45MCA2MS44NSAyMC45MEw2MS44NSAyMC45MFE2Mi44MyAyMC45MCA2My4zNiAyMC4xNVE2My44OSAxOS40MCA2My44OSAxNy45Nkw2My44OSAxNy45Nkw2My44OSAxNy41MVE2My44OSAxNi4wOSA2My4zNiAxNS4zNFE2Mi44MiAxNC41OCA2MS44NCAxNC41OEw2MS44NCAxNC41OFE2MC44OCAxNC41OCA2MC4zMyAxNS4zM1E1OS43OSAxNi4wOSA1OS43OCAxNy40Nkw1OS43OCAxNy40NlpNNzIuMzAgMjJMNjkuODQgMjJMNjkuODQgMTMuNDdMNzIuMzYgMTMuNDdRNzMuNDkgMTMuNDcgNzQuMzcgMTMuOTdRNzUuMjQgMTQuNDggNzUuNzIgMTUuNDBRNzYuMjAgMTYuMzMgNzYuMjAgMTcuNTJMNzYuMjAgMTcuNTJMNzYuMjAgMTcuOTVRNzYuMjAgMTkuMTYgNzUuNzIgMjAuMDhRNzUuMjQgMjEuMDAgNzQuMzQgMjEuNTBRNzMuNDUgMjIgNzIuMzAgMjJMNzIuMzAgMjJaTTcxLjMyIDE0LjY2TDcxLjMyIDIwLjgyTDcyLjI5IDIwLjgyUTczLjQ2IDIwLjgyIDc0LjA4IDIwLjA5UTc0LjcwIDE5LjM2IDc0LjcyIDE3Ljk5TDc0LjcyIDE3Ljk5TDc0LjcyIDE3LjUyUTc0LjcyIDE2LjEzIDc0LjExIDE1LjQwUTczLjUxIDE0LjY2IDcyLjM2IDE0LjY2TDcyLjM2IDE0LjY2TDcxLjMyIDE0LjY2Wk04MC4yMyAxOS40Mkw4MC4yMyAxOS40Mkw4MS43MiAxOS40MlE4MS43MiAyMC4xNSA4Mi4yMCAyMC41NVE4Mi42OCAyMC45NSA4My41NyAyMC45NUw4My41NyAyMC45NVE4NC4zNSAyMC45NSA4NC43NCAyMC42M1E4NS4xMyAyMC4zMiA4NS4xMyAxOS44MEw4NS4xMyAxOS44MFE4NS4xMyAxOS4yNCA4NC43MyAxOC45NFE4NC4zNCAxOC42MyA4My4zMSAxOC4zMlE4Mi4yNyAxOC4wMSA4MS42NiAxNy42M0w4MS42NiAxNy42M1E4MC41MCAxNi45MCA4MC41MCAxNS43Mkw4MC41MCAxNS43MlE4MC41MCAxNC42OSA4MS4zNCAxNC4wMlE4Mi4xOCAxMy4zNSA4My41MiAxMy4zNUw4My41MiAxMy4zNVE4NC40MSAxMy4zNSA4NS4xMSAxMy42OFE4NS44MSAxNC4wMSA4Ni4yMSAxNC42MVE4Ni42MCAxNS4yMiA4Ni42MCAxNS45Nkw4Ni42MCAxNS45Nkw4NS4xMyAxNS45NlE4NS4xMyAxNS4yOSA4NC43MSAxNC45MVE4NC4yOSAxNC41NCA4My41MSAxNC41NEw4My41MSAxNC41NFE4Mi43OCAxNC41NCA4Mi4zOCAxNC44NVE4MS45OCAxNS4xNiA4MS45OCAxNS43MUw4MS45OCAxNS43MVE4MS45OCAxNi4xOCA4Mi40MSAxNi41MFE4Mi44NSAxNi44MSA4My44NCAxNy4xMFE4NC44NCAxNy40MCA4NS40NCAxNy43OFE4Ni4wNSAxOC4xNiA4Ni4zMyAxOC42NVE4Ni42MSAxOS4xMyA4Ni42MSAxOS43OUw4Ni42MSAxOS43OVE4Ni42MSAyMC44NiA4NS43OSAyMS40OVE4NC45NyAyMi4xMiA4My41NyAyMi4xMkw4My41NyAyMi4xMlE4Mi42NSAyMi4xMiA4MS44NyAyMS43N1E4MS4xMCAyMS40MyA4MC42NyAyMC44M1E4MC4yMyAyMC4yMiA4MC4yMyAxOS40MloiIGZpbGw9IiMwMDAwMDAiLz48cGF0aCBjbGFzcz0ic3ZnX190ZXh0IiBkPSIiIGZpbGw9IiMwMDAwMDAiIHg9IjExMS4zOSIvPjwvc3ZnPg==)](https://novelmovementcph.streamlit.app/Methods_%E2%9C%8F%EF%B8%8F_)
[![forthebadge](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI5Mi4yOCIgaGVpZ2h0PSIzNSIgdmlld0JveD0iMCAwIDkyLjI4IDM1Ij48cmVjdCBjbGFzcz0ic3ZnX19yZWN0IiB4PSIwIiB5PSIwIiB3aWR0aD0iOTIuMjgiIGhlaWdodD0iMzUiIGZpbGw9IiNBMUExQTEiLz48cmVjdCBjbGFzcz0ic3ZnX19yZWN0IiB4PSI5Mi4yOCIgeT0iMCIgd2lkdGg9IjAiIGhlaWdodD0iMzUiIGZpbGw9IiM2RkMyREUiLz48cGF0aCBjbGFzcz0ic3ZnX190ZXh0IiBkPSJNMTUuNzAgMjJMMTQuMjIgMjJMMTQuMjIgMTMuNDdMMTcuMjIgMTMuNDdRMTguNjkgMTMuNDcgMTkuNTAgMTQuMTNRMjAuMzAgMTQuNzkgMjAuMzAgMTYuMDVMMjAuMzAgMTYuMDVRMjAuMzAgMTYuOTAgMTkuODkgMTcuNDhRMTkuNDcgMTguMDYgMTguNzMgMTguMzdMMTguNzMgMTguMzdMMjAuNjUgMjEuOTJMMjAuNjUgMjJMMTkuMDYgMjJMMTcuMzUgMTguNzFMMTUuNzAgMTguNzFMMTUuNzAgMjJaTTE1LjcwIDE0LjY2TDE1LjcwIDE3LjUyTDE3LjIyIDE3LjUyUTE3Ljk3IDE3LjUyIDE4LjM5IDE3LjE1UTE4LjgyIDE2Ljc3IDE4LjgyIDE2LjExTDE4LjgyIDE2LjExUTE4LjgyIDE1LjQzIDE4LjQzIDE1LjA1UTE4LjA0IDE0LjY4IDE3LjI2IDE0LjY2TDE3LjI2IDE0LjY2TDE1LjcwIDE0LjY2Wk0zMC4yNyAyMkwyNC42OSAyMkwyNC42OSAxMy40N0wzMC4yMyAxMy40N0wzMC4yMyAxNC42NkwyNi4xOCAxNC42NkwyNi4xOCAxNy4wMkwyOS42OCAxNy4wMkwyOS42OCAxOC4xOUwyNi4xOCAxOC4xOUwyNi4xOCAyMC44MkwzMC4yNyAyMC44MkwzMC4yNyAyMlpNMzQuMDMgMTkuNDJMMzQuMDMgMTkuNDJMMzUuNTIgMTkuNDJRMzUuNTIgMjAuMTUgMzYuMDAgMjAuNTVRMzYuNDggMjAuOTUgMzcuMzcgMjAuOTVMMzcuMzcgMjAuOTVRMzguMTUgMjAuOTUgMzguNTQgMjAuNjNRMzguOTMgMjAuMzIgMzguOTMgMTkuODBMMzguOTMgMTkuODBRMzguOTMgMTkuMjQgMzguNTMgMTguOTRRMzguMTQgMTguNjMgMzcuMTAgMTguMzJRMzYuMDcgMTguMDEgMzUuNDYgMTcuNjNMMzUuNDYgMTcuNjNRMzQuMzAgMTYuOTAgMzQuMzAgMTUuNzJMMzQuMzAgMTUuNzJRMzQuMzAgMTQuNjkgMzUuMTQgMTQuMDJRMzUuOTggMTMuMzUgMzcuMzIgMTMuMzVMMzcuMzIgMTMuMzVRMzguMjEgMTMuMzUgMzguOTEgMTMuNjhRMzkuNjEgMTQuMDEgNDAuMDAgMTQuNjFRNDAuNDAgMTUuMjIgNDAuNDAgMTUuOTZMNDAuNDAgMTUuOTZMMzguOTMgMTUuOTZRMzguOTMgMTUuMjkgMzguNTEgMTQuOTFRMzguMDkgMTQuNTQgMzcuMzEgMTQuNTRMMzcuMzEgMTQuNTRRMzYuNTggMTQuNTQgMzYuMTggMTQuODVRMzUuNzggMTUuMTYgMzUuNzggMTUuNzFMMzUuNzggMTUuNzFRMzUuNzggMTYuMTggMzYuMjEgMTYuNTBRMzYuNjUgMTYuODEgMzcuNjQgMTcuMTBRMzguNjQgMTcuNDAgMzkuMjQgMTcuNzhRMzkuODUgMTguMTYgNDAuMTMgMTguNjVRNDAuNDEgMTkuMTMgNDAuNDEgMTkuNzlMNDAuNDEgMTkuNzlRNDAuNDEgMjAuODYgMzkuNTkgMjEuNDlRMzguNzcgMjIuMTIgMzcuMzcgMjIuMTJMMzcuMzcgMjIuMTJRMzYuNDUgMjIuMTIgMzUuNjcgMjEuNzdRMzQuODkgMjEuNDMgMzQuNDYgMjAuODNRMzQuMDMgMjAuMjIgMzQuMDMgMTkuNDJaTTQ0LjU2IDE5LjE2TDQ0LjU2IDE5LjE2TDQ0LjU2IDEzLjQ3TDQ2LjA0IDEzLjQ3TDQ2LjA0IDE5LjE4UTQ2LjA0IDIwLjAzIDQ2LjQ3IDIwLjQ4UTQ2LjkxIDIwLjkzIDQ3Ljc1IDIwLjkzTDQ3Ljc1IDIwLjkzUTQ5LjQ2IDIwLjkzIDQ5LjQ2IDE5LjEzTDQ5LjQ2IDE5LjEzTDQ5LjQ2IDEzLjQ3TDUwLjk0IDEzLjQ3TDUwLjk0IDE5LjE3UTUwLjk0IDIwLjUzIDUwLjA3IDIxLjMyUTQ5LjIwIDIyLjEyIDQ3Ljc1IDIyLjEyTDQ3Ljc1IDIyLjEyUTQ2LjI5IDIyLjEyIDQ1LjQyIDIxLjMzUTQ0LjU2IDIwLjU1IDQ0LjU2IDE5LjE2Wk02MC44NiAyMkw1NS41MSAyMkw1NS41MSAxMy40N0w1Ni45OSAxMy40N0w1Ni45OSAyMC44Mkw2MC44NiAyMC44Mkw2MC44NiAyMlpNNjYuNjcgMTQuNjZMNjQuMDMgMTQuNjZMNjQuMDMgMTMuNDdMNzAuODAgMTMuNDdMNzAuODAgMTQuNjZMNjguMTQgMTQuNjZMNjguMTQgMjJMNjYuNjcgMjJMNjYuNjcgMTQuNjZaTTc0LjEyIDE5LjQyTDc0LjEyIDE5LjQyTDc1LjYxIDE5LjQyUTc1LjYxIDIwLjE1IDc2LjA5IDIwLjU1UTc2LjU3IDIwLjk1IDc3LjQ2IDIwLjk1TDc3LjQ2IDIwLjk1UTc4LjI0IDIwLjk1IDc4LjYzIDIwLjYzUTc5LjAyIDIwLjMyIDc5LjAyIDE5LjgwTDc5LjAyIDE5LjgwUTc5LjAyIDE5LjI0IDc4LjYyIDE4Ljk0UTc4LjIyIDE4LjYzIDc3LjE5IDE4LjMyUTc2LjE2IDE4LjAxIDc1LjU1IDE3LjYzTDc1LjU1IDE3LjYzUTc0LjM5IDE2LjkwIDc0LjM5IDE1LjcyTDc0LjM5IDE1LjcyUTc0LjM5IDE0LjY5IDc1LjIzIDE0LjAyUTc2LjA3IDEzLjM1IDc3LjQxIDEzLjM1TDc3LjQxIDEzLjM1UTc4LjMwIDEzLjM1IDc5LjAwIDEzLjY4UTc5LjcwIDE0LjAxIDgwLjA5IDE0LjYxUTgwLjQ5IDE1LjIyIDgwLjQ5IDE1Ljk2TDgwLjQ5IDE1Ljk2TDc5LjAyIDE1Ljk2UTc5LjAyIDE1LjI5IDc4LjYwIDE0LjkxUTc4LjE4IDE0LjU0IDc3LjQwIDE0LjU0TDc3LjQwIDE0LjU0UTc2LjY3IDE0LjU0IDc2LjI3IDE0Ljg1UTc1Ljg3IDE1LjE2IDc1Ljg3IDE1LjcxTDc1Ljg3IDE1LjcxUTc1Ljg3IDE2LjE4IDc2LjMwIDE2LjUwUTc2Ljc0IDE2LjgxIDc3LjczIDE3LjEwUTc4LjczIDE3LjQwIDc5LjMzIDE3Ljc4UTc5Ljk0IDE4LjE2IDgwLjIyIDE4LjY1UTgwLjUwIDE5LjEzIDgwLjUwIDE5Ljc5TDgwLjUwIDE5Ljc5UTgwLjUwIDIwLjg2IDc5LjY4IDIxLjQ5UTc4Ljg2IDIyLjEyIDc3LjQ2IDIyLjEyTDc3LjQ2IDIyLjEyUTc2LjU0IDIyLjEyIDc1Ljc2IDIxLjc3UTc0Ljk4IDIxLjQzIDc0LjU1IDIwLjgzUTc0LjEyIDIwLjIyIDc0LjEyIDE5LjQyWiIgZmlsbD0iIzAwMDAwMCIvPjxwYXRoIGNsYXNzPSJzdmdfX3RleHQiIGQ9IiIgZmlsbD0iIzAwMDAwMCIgeD0iMTA1LjI4Ii8+PC9zdmc+)](https://novelmovementcph.streamlit.app/Results_%F0%9F%93%8A)
"""
st.title("Conclusion")
st.markdown(
"""
A significant regression equation was found for novel UE hand movement patterns (F(1,9) = 37.61, p < 0.001), with an R2 of 0.84, but not found for novel UE arm movement patterns. CUE-T scores increased by 12.9 points for each 0.1 increase in mean novel UE hand movement score. Our results indicate that the novel UE movement pattern detection model accurately predicts UE function from a clinical assessment of hand movements in a sample of 10 participants with cervical SCI. 

Novelty detection outcomes may be a robust wearable sensor biomarker to identify different or new movements and monitor function over time. Novelty detection may also aid in the development of personalized care plans to optimize rehabilitation interventions for individuals with cervical SCI.
""")
nd = "https://raw.githubusercontent.com/chags1313/cphresearchday/main/ws.jpg"
st.image(nd, use_column_width=True, caption='AI generated image')

st.title('References')

"""
1. Beekhuizen, Kristina S. PT, PhD. 2005. New Perspectives on Improving Upper Extremity Function after Spinal Cord Injury. Journal of Neurologic Physical Therapy. 
2. Marino RJ, Kern SB, Leiby B, Schmidt-Read M, Mulcahey M. 2015. Reliability and validity of the capabilities of upper extremity test (CUE-T) in subjects with chronic spinal cord injury. The Journal of Spinal Cord Medicine 
3. Mohammadian Rad, N., van Laarhoven, T., Furlanello, C., & Marchiori, E. 2018. Novelty Detection using Deep Normative Modeling for IMU-Based Abnormal Movement Monitoring in Parkinson’s Disease and Autism Spectrum Disorders. Sensors. 
4. Nguyen, T.-N., Huynh, H.-H., & Meunier, J. 2016. Skeleton-Based Abnormal Gait Detection. Sensors, 16(11), 1792. 
5. Khan, S.S., & Taati, B. 2016. Detecting unseen falls from wearable devices using channel-wise ensemble of autoencoders. Expert Syst. Appl., 87, 280-290. 
6. Hiremath SV, Intille SS, Kelleher A, Cooper RA, Ding D. 2015. Detection of physical activities using a physical activity monitor system for wheelchair users. Medical Engineering and Physics; 37(1):68-76. 
7. Ojeda M, Ding D. 2014. Temporal parameters estimation for wheelchair propulsion using wearable sensors. BioMed Research International; 2014. [8] Breunig, M. M.; Kriegel, H.-P.; Ng, R. T.; Sander, J. (2000). LOF: Identifying Density-based Local Outliers (PDF). Proceedings of the 2000 ACM SIGMOD International Conference on Management of Data
"""

