// AI Teaching Platform API Integration
// 支持豆包、文心一言等主流大模型

class AITutor {
    constructor(options = {}) {
        this.apiKey = options.apiKey || '';
        this.apiEndpoint = options.apiEndpoint || 'https://open.bytecloudapi.com/api/v3';
        this.model = options.model || 'doubao-pro-32k';
        this.systemPrompt = options.systemPrompt || this.getDefaultSystemPrompt();
    }

    // 默认系统提示词 - 苏格拉底式教学
    getDefaultSystemPrompt() {
        return `你是一位专业的AI导师，名叫"李彦明AI导师"。你的教学原则：
1. 绝不直接给出答案，而是通过提问引导学生思考
2. 每次回答后给出提示，而不是完整答案
3. 鼓励学生自己推导和发现
4. 使用简单易懂的语言
5. 根据学生水平调整难度
6. 肯定学生的进步，建立自信
7. 只在学生多次尝试后才给出完整解答`;
    }

    // 苏格拉底式引导回答
    async getSocraticResponse(question, userAnswer, hintLevel = 1) {
        const messages = [
            { role: 'system', content: this.systemPrompt },
            { role: 'user', content: `学生问：${question}\n学生答：${userAnswer}` }
        ];

        // 根据提示级别调整指令
        if (hintLevel === 1) {
            messages.push({
                role: 'user',
                content: '请给出第一个提示，引导学生思考，不要直接给答案'
            });
        } else if (hintLevel === 2) {
            messages.push({
                role: 'user',
                content: '学生还没有理解，请给出更具体的提示'
            });
        } else {
            messages.push({
                role: 'user',
                content: '请给出完整解答，但也要解释为什么'
            });
        }

        return this.callAPI(messages);
    }

    // 智能出题
    async generateQuestion(subject, difficulty = 'medium', topic = '') {
        const messages = [
            { role: 'system', content: '你是一位专业的教育出题专家' },
            { role: 'user', content: `请出一道${subject}的${difficulty}难度题目${topic ? '关于' + topic + '的' : ''}，包含题目、答案和3个层次的提示。使用JSON格式返回。` }
        ];

        return this.callAPI(messages);
    }

    // 批改作文
    async gradeEssay(essay, subject = 'chinese') {
        const messages = [
            { role: 'system', content: '你是一位专业的作文批改专家' },
            { role: 'user', content: `请批改这篇${subject === 'chinese' ? '语文' : '英语'}作文，给出评分和改进建议：\n${essay}` }
        ];

        return this.callAPI(messages);
    }

    // 错题分析
    async analyzeWrongQuestion(wrongQ, correctA) {
        const messages = [
            { role: 'system', content: '你是一位学习分析专家' },
            { role: 'user', content: `学生做错了这道题：${wrongQ}\n正确答案是：${correctA}\n请分析错误原因并给出补救建议` }
        ];

        return this.callAPI(messages);
    }

    // 调用API（通用方法）
    async callAPI(messages) {
        try {
            const response = await fetch(`${this.apiEndpoint}/chat/completions`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${this.apiKey}`
                },
                body: JSON.stringify({
                    model: this.model,
                    messages: messages,
                    temperature: 0.7,
                    max_tokens: 1024
                })
            });

            const data = await response.json();
            return data.choices[0].message.content;
        } catch (error) {
            console.error('API调用失败:', error);
            return '抱歉，AI服务暂时不可用，请稍后重试。';
        }
    }

    // 语音识别（浏览器内置）
    startVoiceRecognition(onResult) {
        if (!('webkitSpeechRecognition' in window) && !('SpeechRecognition' in window)) {
            alert('您的浏览器不支持语音识别');
            return null;
        }

        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        const recognition = new SpeechRecognition();
        recognition.lang = 'zh-CN';
        recognition.continuous = false;
        recognition.interimResults = false;

        recognition.onresult = (event) => {
            const transcript = event.results[0][0].transcript;
            onResult(transcript);
        };

        recognition.onerror = (event) => {
            console.error('语音识别错误:', event.error);
        };

        recognition.start();
        return recognition;
    }

    // 语音合成
    speak(text) {
        if ('speechSynthesis' in window) {
            const utterance = new SpeechSynthesisUtterance(text);
            utterance.lang = 'zh-CN';
            utterance.rate = 0.9;
            speechSynthesis.speak(utterance);
        }
    }
}

// 初始化AI导师
const aiTutor = new AITutor({
    apiKey: '', // 需要配置API密钥
    apiEndpoint: 'https://open.bytecloudapi.com/api/v3',
    model: 'doubao-pro-32k'
});

// 导出供其他模块使用
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { AITutor };
}
