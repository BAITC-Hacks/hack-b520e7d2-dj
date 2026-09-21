import os
import sys

FAQ_FILE = "faq.txt"

def load_faq(filepath):
    """Загрузка вопросов и ответов из файла."""
    faq_data = []
    if not os.path.exists(filepath):
        print(f"Ошибка: Файл {filepath} не найден!")
        sys.exit(1)
        
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and "|" in line:
                keywords_raw, answer = line.split("|", 1)
                keywords = [k.strip().lower() for k in keywords_raw.split(",")]
                faq_data.append((keywords, answer.strip()))
    return faq_data

def get_answer(user_query, faq_data):
    """Поиск подходящего ответа по совпадению слов."""
    # Приводим ввод пользователя к нижнему регистру и разбиваем на слова
    query_words = set(user_query.lower().split())
    
    best_answer = None
    max_matches = 0
    
    for keywords, answer in faq_data:
        matches = 0
        for word in query_words:
            # Очищаем слово от базовой пунктуации
            clean_word = word.strip(".,?!:;-")
            for kw in keywords:
                # Проверяем вхождение ключевого слова или подстроки
                if kw in clean_word or clean_word in kw:
                    matches += 1
                    
        if matches > max_matches:
            max_matches = matches
            best_answer = answer
            
    # Если набралось хотя бы 1 совпадение — возвращаем ответ, иначе "не знаю"
    if max_matches > 0:
        return best_answer
    return "Не знаю"

def main():
    faq_data = load_faq(FAQ_FILE)
    print("=== FAQ-бот репетиции HackAlem AI ===")
    print("Задайте вопрос про время, команду, трек, сдачу или призы.")
    print("Для выхода введите 'выход' или 'exit'.\n")
    
    while True:
        try:
            user_input = input("Вы: ").strip()
            if not user_input:
                continue
            if user_input.lower() in ["выход", "exit", "quit"]:
                print("Бот: До свидания!")
                break
                
            answer = get_answer(user_input, faq_data)
            print(f"Бот: {answer}\n")
        except (KeyboardInterrupt, EOFError):
            print("\nБот: До свидания!")
            break

if __name__ == "__main__":
    main()
