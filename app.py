from flask import Flask, render_template, request, redirect
import os

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
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)





# from flask import Flask, render_template, request, redirect, url_for
# import os
# from werkzeug.utils import secure_filename

# app = Flask(__name__)

# # 업로드된 이미지 파일을 저장할 폴더 설정
# UPLOAD_FOLDER = 'static/uploads'
# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # 메모 저장 리스트 (메모와 이미지 파일 경로)
# memos = [] 

# # 이미지 확장자 확인 함수
# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/')
# def index():
#     return render_template('index.html', memos=memos)

# # 메모 추가
# @app.route('/add', methods=['POST'])
# def add_memo():
#     content = request.form['content']
#     file = request.files['image']  # 이미지 파일
#     image_filename = None
    
#     if file and allowed_file(file.filename):
#         filename = secure_filename(file.filename)  # 파일명 보호
#         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))  # 파일 저장
#         image_filename = filename

#     if content or image_filename:  # 메모나 이미지가 있을 때만 추가
#         memos.append({'content': content, 'image': image_filename})
    
#     return redirect('/')

# # 메모 삭제
# @app.route('/delete/<int:memo_index>', methods=['POST'])
# def delete_memo(memo_index):
#     if 0 <= memo_index < len(memos):
#         del memos[memo_index]
#     return redirect('/')

# # 메모 수정 페이지
# @app.route('/edit/<int:memo_index>', methods=['GET', 'POST'])
# def edit_memo(memo_index):
#     if 0 <= memo_index < len(memos):
#         if request.method == 'POST':
#             updated_content = request.form['content']
#             file = request.files['image']  # 수정할 이미지 파일
#             image_filename = memos[memo_index]['image']  # 기존 이미지
            
#             if file and allowed_file(file.filename):
#                 filename = secure_filename(file.filename)
#                 file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#                 image_filename = filename

#             if updated_content or image_filename:
#                 memos[memo_index] = {'content': updated_content, 'image': image_filename}
#             return redirect('/')
        
#         return render_template('edit.html', memo=memos[memo_index], memo_index=memo_index)
#     return redirect('/')

# if __name__ == '__main__':
#     app.run(debug=True)
