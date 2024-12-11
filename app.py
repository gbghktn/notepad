from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# 메모 저장 리스트
memos = [] 

# 메인 페이지
@app.route('/')
def index():
    return render_template('index.html', memos = memos)

# 메모 추가
@app.route('/add', methods=['POST'])
def add_memo():
    content = request.form['content']
    if content and len(content)<=500:  # 빈 메모는 저장하지 않음, 메모의 길이를 500자 이하로 제한
        memos.append(content)
    return redirect('/')

# 메모 삭제
@app.route('/delete/<int:memo_index>', methods=['POST'])
def delete_memo(memo_index):
    if 0 <= memo_index < len(memos):  # 유효한 인덱스인지 확인
        del memos[memo_index]
    return redirect('/')

# 메모 수정 페이지
@app.route('/edit/<int:memo_index>', methods=['GET', 'POST'])
def edit_memo(memo_index):
    if 0 <= memo_index < len(memos):  # 유효한 인덱스인지 확인
        if request.method == 'POST':
            updated_content = request.form['content']
            if updated_content:  # 빈 메모는 저장하지 않음
                memos[memo_index] = updated_content
            return redirect('/')
        return render_template('edit.html', memo=memos[memo_index], memo_index=memo_index)
    return redirect('/')  # 유효하지 않은 인덱스라면 메인 페이지로 리다이렉트

if __name__ == '__main__':
    app.run(debug=True)
