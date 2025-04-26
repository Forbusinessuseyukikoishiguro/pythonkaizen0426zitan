import os
import shutil
from pathlib import Path


def copy_folder_with_numbers(source_folder, target_base_folder, count=31):
    """
    指定されたフォルダを指定回数コピーします。コピー先のフォルダ名には元のフォルダ名に数字を付加します。

    Args:
        source_folder (str): コピー元のフォルダパス
        target_base_folder (str): コピー先の親フォルダパス
        count (int): 作成するコピーの数（デフォルト: 31）
    """
    # パスを Path オブジェクトに変換
    source_path = Path(source_folder)
    target_base_path = Path(target_base_folder)

    # コピー元のフォルダ名を取得
    source_folder_name = source_path.name

    # コピー先の親フォルダが存在しない場合は作成
    if not target_base_path.exists():
        target_base_path.mkdir(parents=True)
        print(f"親フォルダを作成しました: {target_base_path}")

    # 指定回数だけフォルダをコピー
    for i in range(1, count + 1):
        # 新しいフォルダ名 (例: "04hinagata01")
        # 01〜31の2桁表記にするためにzfillを使用
        new_folder_name = f"{source_folder_name}{str(i).zfill(2)}"
        target_path = target_base_path / new_folder_name

        # すでに存在する場合はスキップ
        if target_path.exists():
            print(f"フォルダはすでに存在します: {target_path}")
            continue

        try:
            # フォルダとその中身をコピー
            shutil.copytree(source_path, target_path)
            print(f"コピー完了: {target_path}")
        except Exception as e:
            print(f"コピー中にエラーが発生しました: {e}")


# 実行パラメータ
source_folder = r"C:\Users\yukik\Downloads\20250426_April_daily\04hinagata"
target_base_folder = r"C:\Users\yukik\Downloads\20250426_April_daily"

# スクリプト実行
if __name__ == "__main__":
    # 入力確認
    print(f"コピー元フォルダ: {source_folder}")
    print(f"コピー先親フォルダ: {target_base_folder}")
    print(
        "31個のコピーを作成します。続行するには Enter キーを押してください。中止するには Ctrl+C を押してください。"
    )
    input()

    # 実行
    copy_folder_with_numbers(source_folder, target_base_folder)

    print("完了しました。")
