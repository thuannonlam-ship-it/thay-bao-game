<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Thầy Bảo Đuổi Học Sinh</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #2c3e50;
            color: #fff;
            text-align: center;
            margin: 0;
            padding: 20px;
        }
        #game-container {
            max-width: 600px;
            margin: 0 auto;
            background: #34495e;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 8px 16px rgba(0,0,0,0.3);
        }
        h1 { color: #f1c40f; }
        #status-box {
            font-size: 24px;
            margin: 20px 0;
            padding: 15px;
            border-radius: 8px;
            background: #2c3e50;
        }
        .teacher-alert {
            background: #c0392b !important;
            animation: shake 0.5s;
        }
        .teacher-safe {
            background: #27ae60 !important;
        }
        button {
            background: #e67e22;
            color: white;
            border: none;
            padding: 12px 24px;
            font-size: 18px;
            border-radius: 6px;
            cursor: pointer;
            margin: 10px;
            transition: 0.2s;
        }
        button:hover { background: #d35400; }
        button:active { transform: scale(0.95); }
        #stats {
            display: flex;
            justify-content: space-around;
            font-size: 18px;
            margin-bottom: 20px;
        }
        @keyframes shake {
            0% { transform: translate(1px, 1px) rotate(0deg); }
            20% { transform: translate(-3px, 0px) rotate(-1deg); }
            40% { transform: translate(1px, -1px) rotate(1deg); }
            60% { transform: translate(-3px, 1px) rotate(0deg); }
            80% { transform: translate(1px, -1px) rotate(-1deg); }
            100% { transform: translate(0 narr, 0) rotate(0deg); }
        }
    </style>
</head>
<body>

    <div id="game-container">
        <h1>🏫 Thầy Bảo Đuổi Học Sinh</h1>
        <p>Quy tắc: Khi thầy **Đang Nhìn (Cảnh báo đỏ)**, bạn phải bấm nút **"Cúi Mặt Học Bài"**. Khi thầy **Đi Vắng (Xanh)**, bạn có thể **"Lướt Điện Thoại"** để tích điểm!</p>
        
        <div id="stats">
            <div>Điểm: <span id="score">0</span></div>
            <div>Mạng: <span id="lives">3</span></div>
        </div>

        <div id="status-box" class="teacher-safe">Thầy đang đi vắng. Thoải mái đi! 😎</div>

        <button id="action-btn" onclick="performAction()">📱 Lướt Điện Thoại</button>
        <br>
        <button id="start-btn" onclick="startGame()" style="background: #2980b9;">Bắt Đầu Chơi</button>
    </div>

    <script>
        let score = 0;
        let lives = 3;
        let isPlaying = false;
        let teacherIsLooking = false;
        let gameInterval;
        let stateTimer;

        const statusBox = document.getElementById('status-box');
        const actionBtn = document.getElementById('action-btn');
        const scoreDisplay = document.getElementById('score');
        const livesDisplay = document.getElementById('lives');
        const startBtn = document.getElementById('start-btn');

        function startGame() {
            score = 0;
            lives = 3;
            isPlaying = true;
            startBtn.style.display = 'none';
            updateUI();
            nextState();
        }

        function nextState() {
            if (!isPlaying) return;

            // Ngẫu nhiên trạng thái của thầy (Nhìn hoặc Không nhìn)
            teacherIsLooking = Math.random() < 0.4; // 40% cơ hội thầy quay lại

            if (teacherIsLooking) {
                statusBox.className = 'teacher-alert';
                statusBox.innerHTML = '🚨 THẦY BẢO ĐANG NHÌN! Cúi mặt xuống!';
                actionBtn.innerHTML = '📚 Cúi Mặt Học Bài';
            } else {
                statusBox.className = 'teacher-safe';
                statusBox.innerHTML = '😎 Thầy đang quay đi. Lướt điện thoại thôi!';
                actionBtn.innerHTML = '📱 Lướt Điện Thoại';
            }

            // Thời gian cho mỗi nhịp đổi trạng thái (giảm dần theo điểm nếu muốn khó hơn)
            let waitTime = Math.random() * 2000 + 1500; // 1.5s - 3.5s
            stateTimer = setTimeout(nextState, waitTime);
        }

        function performAction() {
            if (!isPlaying) return;

            if (teacherIsLooking) {
                // Thầy đang nhìn mà dám lướt điện thoại (hoặc bấm nhầm nút) -> Bị phạt!
                lives--;
                statusBox.innerHTML = '❌ BỊ PHÁT HIỆN! Thầy Bảo ghi tên vào sổ đầu bài!';
                if (lives <= 0) {
                    endGame();
                }
            } else {
                // An toàn, cộng điểm
                score += 10;
                statusBox.innerHTML = '✅ An toàn! Tích lũy được điểm.';
            }
            updateUI();
        }

        function updateUI() {
            scoreDisplay.innerText = score;
            livesDisplay.innerText = lives;
        }

        function endGame() {
            isPlaying = false;
            clearTimeout(stateTimer);
            statusBox.className = 'teacher-alert';
            statusBox.innerHTML = `GAME OVER! Bạn đã bị đuổi học. Tổng điểm: ${score}`;
            actionBtn.innerHTML = 'Chơi Lại';
            startBtn.style.display = 'inline-block';
            startBtn.innerText = 'Chơi Lại';
        }
    </script>

</body>
</html>
