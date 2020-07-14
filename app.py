from flask import Flask, request, render_template, jsonify, session
from musicdl import musicdl

# session configuraiton -- filesystem interface
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
# SESSION_TYPE = 'filesystem'
# app.config.from_object(__name__)
# Session(app)

def get_or_session(s=None):
    if not session.get('search_size_per_source'):
        session['search_size_per_source'] = 5
    if s:
        session['search_size_per_source'] = s
    return session.get('search_size_per_source')
  

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
        s = request.get_json()
        get_or_session(s.get('search_size_per_source'))
        print(get_or_session())
        config = {'logfilepath': 'musicdl.log', 'savedir': 'downloaded', 'search_size_per_source': get_or_session(), 'proxies': {}}
        target_srcs = s.get('target_srcs')
        client = musicdl.musicdl(config=config)
        search_results = client.search(s.get('search_data'), target_srcs)
        print(search_results)
        return jsonify({'result': search_results})
    else:
        return 'Method Not Allowed'

@app.route('/download', methods=['POST'])
def download():
    if request.method == 'POST':
        s = request.get_json()
        print(s)
        config = {'logfilepath': 'musicdl.log', 'savedir': 'downloaded', 'search_size_per_source': get_or_session(), 'proxies': {}}
        client = musicdl.musicdl(config=config)
        client.download(s)
        return ''
    else:
        return 'Method Not AlloweddataidatVjvuuuida'

@app.route('/set_session', methods=['POST'])
def set():
    if request.method == 'POST':
        s = request.get_json()
        get_or_session(s.get('search_size_per_source'))
        return ''