# yutube_ios_streamlit_app

import streamlit as st
from yt_dlp import YoutubeDL

st.set_page_config(page_title="📱 iOS向け動画ダウンロード", layout="centered")

st.title("📥 iOS専用 動画ダウンロードリンク生成")
st.markdown("\u4ee5\u4e0b\u306b\u52d5\u753b\u306eURL\u3092\u5165\u529b\u3057\u3066\u304f\u3060\u3055\u3044\u3002iOS Safari\u3067\u518d\u751f\u30fb\u9577\u6295\u3057\u4fdd\u5b58\u304c\u53ef\u80fd\u3067\u3059。")

url = st.text_input("🎮 動画URLを入力", placeholder="https://www.youtube.com/watch?v=XXXXXXX")

if st.button("🔗 ダウンロードリンクを取得"):
    if not url.strip():
        st.warning("URLを入力してください。")
    else:
        with st.spinner("動画情報を取得中..."):
            try:
                ydl_opts = {
                    'quiet': True,
                    'skip_download': True,
                    'noplaylist': True,
                    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
                }
                with YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=False)
                    video_url = info.get("url")
                    title = info.get("title", "video")

                if video_url:
                    st.success("✅ ダウンロードリンクを取得しました！")
                    st.video(video_url)
                    st.markdown(f"[\ud83d\udce5 長投して保存: {title}]({video_url})", unsafe_allow_html=True)
                else:
                    st.error("❌ 再生可能なリンクが見つかりませんでした。")
            except Exception as e:
                st.error(f"❌ エラーが発生しました: {e}")

                else:
                    st.error("❌ 再生可能なリンクが見つかりませんでした。")
            except Exception as e:
                st.error(f"❌ エラーが発生しました: {e}")
