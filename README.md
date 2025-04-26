# pythonkaizen0426zitan
note公開用業務改善Pythonコード

# Pythonフォルダコピースクリプト徹底解説 - 新人エンジニア向けガイド

こんにちは、新人エンジニアの皆さん！今回は、Pythonを使ったフォルダ複製スクリプトをステップバイステップで解説します。このスクリプトは、テンプレートフォルダを自動的に複数コピーして、連番を付けるという実用的な機能を持っています。実務でよく発生するこのような作業を自動化することで、効率向上に大きく貢献します。
Use Control + Shift + m to toggle the tab key moving focus. Alternatively, use esc then tab to move to the next interactive element on the page.
選択されていません
Attach files by dragging & dropping, selecting or pasting them.
Editing pythonkaizen0426zitan/README.md at main · Forbusinessuseyukikoishiguro/pythonkaizen0426zitan

翻訳


## コード全体解説

まずはコード全体を見てから、一行ずつ解説していきましょう。

```python
import os  # OSに関する操作（ファイル・ディレクトリ操作など）を行うモジュールをインポート
import shutil  # 高水準のファイル操作（コピーなど）を行うモジュールをインポート
from pathlib import Path  # パス操作を簡単に行うためのPathクラスをインポート

def copy_folder_with_numbers(source_folder, target_base_folder, count=31):
    """
    指定されたフォルダを指定回数コピーします。コピー先のフォルダ名には元のフォルダ名に数字を付加します。
    
    Args:
        source_folder (str): コピー元のフォルダパス
        target_base_folder (str): コピー先の親フォルダパス
        count (int): 作成するコピーの数（デフォルト: 31）
    """
    # パスを Path オブジェクトに変換
    source_path = Path(source_folder)  # コピー元のパスをPathオブジェクトに変換
    target_base_path = Path(target_base_folder)  # コピー先の親フォルダのパスをPathオブジェクトに変換
    
    # コピー元のフォルダ名を取得
    source_folder_name = source_path.name  # Pathオブジェクトから最後のフォルダ名部分だけを取得
    
    # コピー先の親フォルダが存在しない場合は作成
    if not target_base_path.exists():  # 親フォルダが存在しないかチェック
        target_base_path.mkdir(parents=True)  # 親フォルダと必要な中間フォルダを全て作成
        print(f"親フォルダを作成しました: {target_base_path}")  # 作成完了メッセージを表示
    
    # 指定回数だけフォルダをコピー
    for i in range(1, count + 1):  # 1からcount（デフォルト31）までの数値でループ
        # 新しいフォルダ名 (例: "04hinagata01")
        # 01〜31の2桁表記にするためにzfillを使用
        new_folder_name = f"{source_folder_name}{str(i).zfill(2)}"  # 元フォルダ名+連番(2桁)の名前を作成
        target_path = target_base_path / new_folder_name  # コピー先のフルパスを作成（Pathオブジェクトは/演算子でパスを結合できる）
        
        # すでに存在する場合はスキップ
        if target_path.exists():  # コピー先パスが既に存在するか確認
            print(f"フォルダはすでに存在します: {target_path}")  # 既存のフォルダがあることを通知
            continue  # forループの次の繰り返しに進む（現在の処理をスキップ）
        
        try:
            # フォルダとその中身をコピー
            shutil.copytree(source_path, target_path)  # フォルダとその中身を丸ごとコピー
            print(f"コピー完了: {target_path}")  # コピー成功を通知
        except Exception as e:  # どんなエラーが発生しても捕捉
            print(f"コピー中にエラーが発生しました: {e}")  # エラー内容を表示

# 実行パラメータ
source_folder = r"C:\Users\yukik\Downloads\20250426_April_daily\04hinagata"  # コピー元フォルダのパス（r プレフィックスで生文字列指定）
target_base_folder = r"C:\Users\yukik\Downloads\20250426_April_daily"  # コピー先親フォルダのパス

# スクリプト実行
if __name__ == "__main__":  # このファイルが直接実行された場合にのみ以下のコードを実行
    # 入力確認
    print(f"コピー元フォルダ: {source_folder}")  # 処理内容の確認表示（コピー元）
    print(f"コピー先親フォルダ: {target_base_folder}")  # 処理内容の確認表示（コピー先）
    print(
        "31個のコピーを作成します。続行するには Enter キーを押してください。中止するには Ctrl+C を押してください。"
    )  # 実行前の確認メッセージを表示
    input()  # ユーザーからの入力を待機（Enter キーで続行）
    
    # 実行
    copy_folder_with_numbers(source_folder, target_base_folder)  # 定義した関数を実行
    
    print("完了しました。")  # 処理完了を通知
```

## 1行ずつの詳細解説

### モジュールのインポート

```python
import os
```
- OSに関する基本的な操作（ファイル・ディレクトリ操作、環境変数アクセスなど）を行うためのモジュールをインポートします。
- このスクリプトでは直接使用していませんが、shutil や pathlib が内部で使用するために必要です。

```python
import shutil
```
- 「shell utilities」の略で、ファイルやディレクトリの高水準操作（コピー、移動、削除など）を提供するモジュールです。
- 特にこのスクリプトでは `copytree()` 関数を使用して、ディレクトリとその中身を再帰的にコピーします。

```python
from pathlib import Path
```
- オブジェクト指向でファイルシステムパスを操作するための `Path` クラスだけをインポートします。
- 従来の `os.path` より直感的にパス操作ができます（連結、親ディレクトリ取得、存在チェックなど）。

### 関数の定義

```python
def copy_folder_with_numbers(source_folder, target_base_folder, count=31):
```
- `copy_folder_with_numbers` という関数を定義します。
- 3つのパラメータを受け取ります：
  - `source_folder`: コピー元のフォルダのパス（文字列）
  - `target_base_folder`: コピー先の親フォルダのパス（文字列）
  - `count`: 作成するコピーの数（デフォルト値は31）

```python
"""
指定されたフォルダを指定回数コピーします。コピー先のフォルダ名には元のフォルダ名に数字を付加します。
    
Args:
    source_folder (str): コピー元のフォルダパス
    target_base_folder (str): コピー先の親フォルダパス
    count (int): 作成するコピーの数（デフォルト: 31）
"""
```
- これはドキュメンテーション文字列（docstring）です。関数の機能とパラメータを説明します。
- Google Styleのドキュメント形式を採用しており、コード補完や自動ドキュメント生成ツールが利用できます。

### パスの準備

```python
source_path = Path(source_folder)
```
- 文字列で受け取ったコピー元のパスを `Path` オブジェクトに変換します。
- `Path` オブジェクトを使うことで、OSに依存しないパス操作が可能になります。

```python
target_base_path = Path(target_base_folder)
```
- 同様に、コピー先の親フォルダのパスも `Path` オブジェクトに変換します。

```python
source_folder_name = source_path.name
```
- `source_path` から最後のコンポーネント（フォルダ名部分）だけを取得します。
- 例えば、`C:\Users\yukik\Downloads\20250426_April_daily\04hinagata` から `04hinagata` を取得します。

### 親フォルダの確認と作成

```python
if not target_base_path.exists():
```
- コピー先の親フォルダが存在するかどうかをチェックします。
- `exists()` メソッドはパスが存在する場合に `True` を返します。

```python
target_base_path.mkdir(parents=True)
```
- 親フォルダが存在しない場合、それを作成します。
- `parents=True` オプションにより、必要な親ディレクトリも全て作成されます（例：`/a/b/c` を作る際に `/a` と `/a/b` も必要なら作成）。

```python
print(f"親フォルダを作成しました: {target_base_path}")
```
- 親フォルダを作成したことをユーザーに通知します。
- f-string（フォーマット済み文字列リテラル）を使用して変数をメッセージに埋め込んでいます。

### フォルダのコピー処理

```python
for i in range(1, count + 1):
```
- 1から `count`（デフォルトでは31）までの数値でループします。
- これにより、01から31までの番号付きコピーを作成します。

```python
new_folder_name = f"{source_folder_name}{str(i).zfill(2)}"
```
- 新しいフォルダ名を作成します。元のフォルダ名に数字を追加します。
- `zfill(2)` は数字を文字列にして、2桁になるよう左側を0で埋めます（例：1→01、2→02）。

```python
target_path = target_base_path / new_folder_name
```
- コピー先のフルパスを作成します。
- `Path` オブジェクトでは、`/` 演算子を使ってパスを連結できます（OS依存の区切り文字を気にする必要がない）。

### 既存フォルダのチェックとスキップ

```python
if target_path.exists():
```
- コピー先のパスが既に存在するかをチェックします。

```python
print(f"フォルダはすでに存在します: {target_path}")
```
- 既に存在する場合は、そのことをユーザーに通知します。

```python
continue
```
- `continue` 文によりループの残りの部分をスキップし、次の繰り返しに進みます。
- これにより、既存のフォルダを上書きせずに処理を続行できます。

### フォルダのコピーと例外処理

```python
try:
```
- `try` ブロックを開始し、エラーが発生する可能性のあるコードを囲みます。

```python
shutil.copytree(source_path, target_path)
```
- `shutil.copytree()` 関数を使用して、フォルダとその中身を再帰的にコピーします。
- ソースディレクトリ全体が、指定した宛先に対して、すべてのファイルとサブディレクトリを含めてコピーされます。

```python
print(f"コピー完了: {target_path}")
```
- コピーが成功したことをユーザーに通知します。

```python
except Exception as e:
```
- どんな種類の例外（エラー）でもキャッチします。
- 例外情報は変数 `e` に格納されます。

```python
print(f"コピー中にエラーが発生しました: {e}")
```
- エラーが発生した場合、その詳細をユーザーに通知します。
- これにより、プログラムが途中で終了せず、問題を特定しやすくなります。

### 実行パラメータの設定

```python
source_folder = r"C:\Users\yukik\Downloads\20250426_April_daily\04hinagata"
```
- コピー元フォルダのパスを指定します。
- `r` プレフィックスはraw文字列リテラルを示し、バックスラッシュをエスケープ文字として扱わないようにします。
- Windowsのパスでは重要です（`\` がエスケープシーケンスと解釈されるのを防ぐため）。

```python
target_base_folder = r"C:\Users\yukik\Downloads\20250426_April_daily"
```
- コピー先の親フォルダのパスを指定します。
- コピーしたフォルダはこの親フォルダ内に作成されます。

### メイン実行部分

```python
if __name__ == "__main__":
```
- このスクリプトが直接実行された場合にのみ以下のコードを実行します。
- 他のスクリプトからインポートされた場合は実行されません。
- Pythonの一般的なイディオム（慣用的な書き方）で、モジュールとスクリプトの両方として機能するように書くときに使用します。

```python
print(f"コピー元フォルダ: {source_folder}")
print(f"コピー先親フォルダ: {target_base_folder}")
```
- 処理を始める前に、ユーザーにコピー元とコピー先を表示して確認させます。

```python
print("31個のコピーを作成します。続行するには Enter キーを押してください。中止するには Ctrl+C を押してください。")
```
- ユーザーに確認を求めるメッセージを表示します。
- 大量のファイル操作を行う前の安全措置として機能します。

```python
input()
```
- ユーザーからの入力を待ちます。
- ユーザーがEnterキーを押すまでプログラムは次に進みません。
- 入力内容自体は使用されませんが、処理を続行するかどうかの判断ポイントとなります。

```python
copy_folder_with_numbers(source_folder, target_base_folder)
```
- 定義した関数を呼び出して、フォルダのコピー処理を実行します。
- パラメータには前に定義した値を使用しています。

```python
print("完了しました。")
```
- すべての処理が終了したことをユーザーに通知します。

## 実践的なポイント

### 1. パスの扱い方
- `pathlib.Path` を使うことで、OSに依存しないパス操作が可能になります。
- Windowsでは `\`、UNIX系では `/` という違いを吸収してくれます。

### 2. エラーハンドリング
- `try`/`except` を使うことで、エラーが発生してもプログラムが強制終了せず処理を続行できます。
- 特に複数のファイル操作を行う場合は重要です。

### 3. ユーザーインターフェース
- 実行前に確認を求めることで、誤操作を防ぎます。
- 処理状況を適宜表示することで、ユーザーに進捗が分かるようにしています。

### 4. モジュール性
- 機能を関数としてカプセル化することで、再利用性が高まります。
- パラメータを変更するだけで、様々な用途に応用できます。

## まとめ

このスクリプトは、単純ながらも実務で非常に役立つ機能を提供します。特に以下のような状況で活用できます：

1. 日次/月次のレポートフォルダの作成
2. プロジェクトテンプレートの展開
3. バックアップフォルダの管理
4. テスト環境の複数セットアップ

Pythonの基本的な機能を使いこなすことで、単調で時間のかかる作業を自動化し、業務効率を大幅に向上させることができます。

このスクリプトを理解し、自分の業務に合わせてカスタマイズしてみてください。プログラミングの力で、日々の業務をより効率的に進めましょう！

＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃３
中間フォルダの作成と、コピーの挙動について、もう少し詳しく説明しますね。

## 中間フォルダの作成機能

スクリプト内の以下の部分に注目してください：

```python
# コピー先の親フォルダが存在しない場合は作成
if not target_base_path.exists():
    target_base_path.mkdir(parents=True)
    print(f"親フォルダを作成しました: {target_base_path}")
```

ここでの `parents=True` パラメータが重要です：

- `parents=True` を指定すると、指定したパスに至るまでの全ての親ディレクトリが存在しない場合に、それらも含めて自動的に作成されます。
- 例えば、`C:\Users\yukik\Downloads\20250426_April_daily` を作成しようとした時に、`C:\Users\yukik\Downloads` が存在しなかった場合でも、必要なフォルダを全て作成します。
- この機能がない場合（`parents=False` またはデフォルト）は、親ディレクトリが存在しないと `FileNotFoundError` が発生します。

## コピーの挙動

スクリプトのコピー処理は `shutil.copytree()` 関数を使用しています：

```python
shutil.copytree(source_path, target_path)
```

この `copytree()` 関数の挙動を詳しく説明すると：

1. **完全な再帰コピー**：ソースフォルダと、そのフォルダ内の全てのファイル、全てのサブフォルダ（とその中のファイル）を再帰的にコピーします。

2. **ターゲットの事前確認**：コピー先のフォルダが既に存在する場合、デフォルトではエラーになります（このスクリプトでは先に存在確認をして、存在する場合はスキップしています）。

3. **メタデータの保持**：ファイルのパーミッション、タイムスタンプなどのメタデータもコピーされます。

4. **シンボリックリンクの扱い**：デフォルトでは、シンボリックリンクはリンクとしてコピーされます（リンク先の実体はコピーされません）。

5. **エラーハンドリング**：コピー中に発生した例外は、このスクリプトでは `try-except` ブロックで捕捉し、メッセージを表示して次のフォルダの処理に進みます。

もし特定のファイルやサブフォルダをコピーから除外したい場合は、`shutil.copytree()` の追加パラメータ `ignore` を使用することもできます。例えば：

```python
# .gitフォルダと.tmpファイルを除外する例
from shutil import ignore_patterns
shutil.copytree(source_path, target_path, ignore=ignore_patterns('*.git', '*.tmp'))
```

中間フォルダの作成と、コピーの挙動について、もう少し詳しく説明しますね。

## 中間フォルダの作成機能

スクリプト内の以下の部分に注目してください：

```python
# コピー先の親フォルダが存在しない場合は作成
if not target_base_path.exists():
    target_base_path.mkdir(parents=True)
    print(f"親フォルダを作成しました: {target_base_path}")
```

ここでの `parents=True` パラメータが重要です：

- `parents=True` を指定すると、指定したパスに至るまでの全ての親ディレクトリが存在しない場合に、それらも含めて自動的に作成されます。
- 例えば、`C:\Users\yukik\Downloads\20250426_April_daily` を作成しようとした時に、`C:\Users\yukik\Downloads` が存在しなかった場合でも、必要なフォルダを全て作成します。
- この機能がない場合（`parents=False` またはデフォルト）は、親ディレクトリが存在しないと `FileNotFoundError` が発生します。

## コピーの挙動

スクリプトのコピー処理は `shutil.copytree()` 関数を使用しています：

```python
shutil.copytree(source_path, target_path)
```

この `copytree()` 関数の挙動を詳しく説明すると：

1. **完全な再帰コピー**：ソースフォルダと、そのフォルダ内の全てのファイル、全てのサブフォルダ（とその中のファイル）を再帰的にコピーします。

2. **ターゲットの事前確認**：コピー先のフォルダが既に存在する場合、デフォルトではエラーになります（このスクリプトでは先に存在確認をして、存在する場合はスキップしています）。

3. **メタデータの保持**：ファイルのパーミッション、タイムスタンプなどのメタデータもコピーされます。

4. **シンボリックリンクの扱い**：デフォルトでは、シンボリックリンクはリンクとしてコピーされます（リンク先の実体はコピーされません）。

5. **エラーハンドリング**：コピー中に発生した例外は、このスクリプトでは `try-except` ブロックで捕捉し、メッセージを表示して次のフォルダの処理に進みます。

もし特定のファイルやサブフォルダをコピーから除外したい場合は、`shutil.copytree()` の追加パラメータ `ignore` を使用することもできます。例えば：

```python
# .gitフォルダと.tmpファイルを除外する例
from shutil import ignore_patterns
shutil.copytree(source_path, target_path, ignore=ignore_patterns('*.git', '*.tmp'))
```

このように、`pathlib.Path` と `shutil.copytree()` を組み合わせることで、柔軟かつ安全なフォルダコピー操作が実現できます。

このように、`pathlib.Path` と `shutil.copytree()` を組み合わせることで、柔軟かつ安全なフォルダコピー操作が実現できます。
