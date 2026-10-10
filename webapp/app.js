const tg = window.Telegram.WebApp;
tg.expand();

let player = {
    hp: 100,
    water: 50,
    loot: 0,
    currentNode: "start"
};

const storyNodes = {
    "start": {
        text: "Ты пришел в себя в заброшенном бункере. В воздухе пахнет сыростью и газом. На полу лежит старый лом, а впереди — тёмный коридор.",
        choices: [
            { text: "🛠 Взять лом и идти дальше", next: "corridor", hpDelta: 0, waterDelta: -5, lootDelta: 1 },
            { text: "🏃 Осмотреть вентиляционную шахту", next: "vent", hpDelta: -25, waterDelta: -5, lootDelta: 0 }
        ]
    },
    "corridor": {
        text: "В коридоре ты встречаешь одичавшую собаку-мутанта! Она скалится и готовится к прыжку.",
        choices: [
            { text: "⚔️ Отбиться ломом", next: "win_fight", hpDelta: -20, waterDelta: -5, lootDelta: 2 },
            { text: "🚪 Забежать в боковую комнату", next: "room", hpDelta: -5, waterDelta: -10, lootDelta: 0 }
        ]
    },
    "vent": {
        text: "Вентиляция оказалась гнилой! Ты сорвался вниз, сильно ударился о металлические трубы и потерял сознание...",
        choices: [
            { text: "🔄 Прийти в себя и встать", next: "start", hpDelta: -30, waterDelta: -10, lootDelta: 0 }
        ]
    },
    "room": {
        text: "Ты заперся в старой кладовой. Здесь темно, но на стеллажах валяется герметичная бутыль с водой.",
        choices: [
            { text: "💧 Выпить воду и отдохнуть (+30 Вода, +10 HP)", next: "start", hpDelta: +10, waterDelta: +30, lootDelta: 1 }
        ]
    },
    "win_fight": {
        text: "Ты победил мутанта! В рюкзаке убитого мародера нашелся ценный лут. Путь наружу свободен.",
        choices: [
            { text: "🌅 Выйти на поверхность Пустоши", next: "start", hpDelta: +20, waterDelta: +20, lootDelta: 5 }
        ]
    }
};

function updateUI() {
    document.getElementById('hp').innerText = player.hp;
    document.getElementById('water').innerText = player.water;
    document.getElementById('loot').innerText = player.loot;

    const node = storyNodes[player.currentNode] || storyNodes["start"];
    document.getElementById('story-text').innerText = node.text;

    // Подгружаем картинку под текущий узел
    const imgElement = document.getElementById('story-image');
    imgElement.src = `https://picsum.photos/seed/${player.currentNode}/400/200`;

    const choicesContainer = document.getElementById('choices-container');
    choicesContainer.innerHTML = '';

    node.choices.forEach(choice => {
        const btn = document.createElement('button');
        btn.className = 'btn-choice';
        btn.innerText = choice.text;
        btn.onclick = () => makeChoice(choice);
        choicesContainer.appendChild(btn);
    });
}

function makeChoice(choice) {
    player.hp += choice.hpDelta;
    player.water += choice.waterDelta;
    player.loot += choice.lootDelta;

    // Ограничиваем здоровье максимум 100 HP
    if (player.hp > 100) {
        player.hp = 100;
    }

    // Проверка на проигрыш (0 HP)
    if (player.hp <= 0) {
        player.hp = 0;
        updateUI();
        alert("☠️ Твое здоровье упало до нуля... Пустошь забрала тебя. Игра окончена.");
        resetGame();
        return;
    }

    player.currentNode = choice.next;
    updateUI();
}

function resetGame() {
    player.hp = 100;
    player.water = 50;
    player.loot = 0;
    player.currentNode = "start";
    updateUI();
}

updateUI();
