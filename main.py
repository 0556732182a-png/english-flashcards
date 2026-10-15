import random
import tkinter as tk

def rev(text):
    if any("\u0590" <= c <= "\u05fe" for c in text):
        return text[::-1]
    return text

WORDS = [
    {"id": 1, "word": "the", "translation": "ה' הידיעה"},
    {"id": 2, "word": "be", "translation": "להיות"},
    {"id": 3, "word": "to", "translation": "ל... / אל"},
    {"id": 4, "word": "of", "translation": "של"},
    {"id": 5, "word": "and", "translation": "ו... (חיבור)"},
    {"id": 6, "word": "a", "translation": "א / אחד"},
    {"id": 7, "word": "in", "translation": "בתוך / ב..."},
    {"id": 8, "word": "that", "translation": "ההוא / ש..."},
    {"id": 9, "word": "have", "translation": "יש / לאכול"},
    {"id": 10, "word": "I", "translation": "אני"},
    {"id": 11, "word": "it", "translation": "זה / זהו"},
    {"id": 12, "word": "for", "translation": "בשביל / עבור"},
    {"id": 13, "word": "not", "translation": "לא"},
    {"id": 14, "word": "on", "translation": "על"},
    {"id": 15, "word": "with", "translation": "עם"},
    {"id": 16, "word": "he", "translation": "הוא"},
    {"id": 17, "word": "as", "translation": "כמו / כפי ש..."},
    {"id": 18, "word": "you", "translation": "אתה / את / אתם"},
    {"id": 19, "word": "do", "translation": "לעשות"},
    {"id": 20, "word": "at", "translation": "ב... (מיקום/זמן)"},
    {"id": 21, "word": "this", "translation": "הזה"},
    {"id": 22, "word": "but", "translation": "אבל"},
    {"id": 23, "word": "his", "translation": "שלו"},
    {"id": 24, "word": "by", "translation": "על ידי / ליד"},
    {"id": 25, "word": "from", "translation": "מ... / מאיפה"},
    {"id": 26, "word": "they", "translation": "הם / הן"},
    {"id": 27, "word": "we", "translation": "אנחנו"},
    {"id": 28, "word": "say", "translation": "לומר"},
    {"id": 29, "word": "her", "translation": "שלה / אותה"},
    {"id": 30, "word": "she", "translation": "היא"},
    {"id": 31, "word": "or", "translation": "או"},
    {"id": 32, "word": "an", "translation": "א (לפני אות ניקוד)"},
    {"id": 33, "word": "will", "translation": "יקרה (עתיד) / רצון"},
    {"id": 34, "word": "my", "translation": "שלי"},
    {"id": 35, "word": "one", "translation": "אחד"},
    {"id": 36, "word": "all", "translation": "הכל / כל"},
    {"id": 37, "word": "would", "translation": "היה... (התניה)"},
    {"id": 38, "word": "there", "translation": "שם"},
    {"id": 39, "word": "their", "translation": "שלהם / שלהן"},
    {"id": 40, "word": "what", "translation": "מה"},
    {"id": 41, "word": "so", "translation": "אז / כל כך"},
    {"id": 42, "word": "up", "translation": "למעלה"},
    {"id": 43, "word": "out", "translation": "בחוץ / החוצה"},
    {"id": 44, "word": "if", "translation": "אם"},
    {"id": 45, "word": "about", "translation": "על / בערך"},
    {"id": 46, "word": "who", "translation": "מי"},
    {"id": 47, "word": "get", "translation": "לקבל / להגיע"},
    {"id": 48, "word": "which", "translation": "איזה / אשר"},
    {"id": 49, "word": "go", "translation": "ללכת"},
    {"id": 50, "word": "me", "translation": "אותי / לי"},
    {"id": 51, "word": "when", "translation": "מתי / כאשר"},
    {"id": 52, "word": "make", "translation": "לעשות / ליצור"},
    {"id": 53, "word": "can", "translation": "יכול"},
    {"id": 54, "word": "like", "translation": "כמו / לאהוב"},
    {"id": 55, "word": "time", "translation": "זמן / פעם"},
    {"id": 56, "word": "no", "translation": "לא / שום"},
    {"id": 57, "word": "just", "translation": "רק / בדיוק"},
    {"id": 58, "word": "him", "translation": "אותו"},
    {"id": 59, "word": "know", "translation": "לדעת"},
    {"id": 60, "word": "take", "translation": "לקחת"},
    {"id": 61, "word": "people", "translation": "אנשים"},
    {"id": 62, "word": "into", "translation": "לתוך"},
    {"id": 63, "word": "year", "translation": "שנה"},
    {"id": 64, "word": "your", "translation": "שלך / שלכם"},
    {"id": 65, "word": "good", "translation": "טוב"},
    {"id": 66, "word": "some", "translation": "כמה / קצת"},
    {"id": 67, "word": "could", "translation": "יכול היה"},
    {"id": 68, "word": "them", "translation": "אותם / אותן"},
    {"id": 69, "word": "see", "translation": "לראות"},
    {"id": 70, "word": "other", "translation": "אחר"},
    {"id": 71, "word": "than", "translation": "מאשר (להשוואה)"},
    {"id": 72, "word": "then", "translation": "אז / אחר כך"},
    {"id": 73, "word": "now", "translation": "עכשיו"},
    {"id": 74, "word": "look", "translation": "להסתכל / נראה"},
    {"id": 75, "word": "only", "translation": "רק"},
    {"id": 76, "word": "come", "translation": "לבוא"},
    {"id": 77, "word": "its", "translation": "שלו/שלה (עבור חפץ/חיה)"},
    {"id": 78, "word": "over", "translation": "מעל / נגמר"},
    {"id": 79, "word": "think", "translation": "לחשוב"},
    {"id": 80, "word": "also", "translation": "גם"},
    {"id": 81, "word": "back", "translation": "בחזרה"},
    {"id": 82, "word": "after", "translation": "אחרי"},
    {"id": 83, "word": "use", "translation": "להשתמש / שימוש"},
    {"id": 84, "word": "two", "translation": "שניים"},
    {"id": 85, "word": "how", "translation": "איך"},
    {"id": 86, "word": "our", "translation": "שלנו"},
    {"id": 87, "word": "work", "translation": "לעבוד / עבודה"},
    {"id": 88, "word": "first", "translation": "ראשון"},
    {"id": 89, "word": "well", "translation": "היטב / טוב נו"},
    {"id": 90, "word": "way", "translation": "דרך"},
    {"id": 91, "word": "even", "translation": "אפילו"},
    {"id": 92, "word": "new", "translation": "חדש"},
    {"id": 93, "word": "want", "translation": "לרצות"},
    {"id": 94, "word": "because", "translation": "בגלל ש..."},
    {"id": 95, "word": "any", "translation": "כל / כלשהו"},
    {"id": 96, "word": "these", "translation": "האלה"},
    {"id": 97, "word": "give", "translation": "לתת"},
    {"id": 98, "word": "day", "translation": "יום"},
    {"id": 99, "word": "most", "translation": "הכי / רוב"},
    {"id": 100, "word": "us", "translation": "אותנו"},
    {"id": 101, "word": "is", "translation": "הינו / נמצא"},
    {"id": 102, "word": "was", "translation": "היה"},
    {"id": 103, "word": "are", "translation": "הינם / נמצאים"},
    {"id": 104, "word": "been", "translation": "היה (זמן מושלם)"},
    {"id": 105, "word": "has", "translation": "יש לו/לה"},
    {"id": 106, "word": "had", "translation": "היה לו/לה"},
    {"id": 107, "word": "more", "translation": "יותר"},
    {"id": 108, "word": "find", "translation": "למצוא"},
    {"id": 109, "word": "here", "translation": "כאן"},
    {"id": 110, "word": "thing", "translation": "דבר"},
    {"id": 111, "word": "many", "translation": "הרבה (ספיר)"},
    {"id": 112, "word": "tell", "translation": "לספר / להגיד"},
    {"id": 113, "word": "very", "translation": "מאוד"},
    {"id": 114, "word": "woman", "translation": "אישה"},
    {"id": 115, "word": "through", "translation": "דרך / באמצעות"},
    {"id": 116, "word": "life", "translation": "חיים"},
    {"id": 117, "word": "child", "translation": "ילד"},
    {"id": 118, "word": "down", "translation": "למטה"},
    {"id": 119, "word": "may", "translation": "עשוי / אולי"},
    {"id": 120, "word": "should", "translation": "צריך / כדאי"},
    {"id": 121, "word": "call", "translation": "להתקשר / לקרוא ל..."},
    {"id": 122, "word": "world", "translation": "עולם"},
    {"id": 123, "word": "school", "translation": "בית ספר"},
    {"id": 124, "word": "still", "translation": "עדיין"},
    {"id": 125, "word": "try", "translation": "לנסות"},
    {"id": 126, "word": "last", "translation": "אחרון"},
    {"id": 127, "word": "ask", "translation": "לשאול / לבקש"},
    {"id": 128, "word": "need", "translation": "להזדקק / צורך"},
    {"id": 129, "word": "too", "translation": "גם / מדי"},
    {"id": 130, "word": "feel", "translation": "להרגיש"},
    {"id": 131, "word": "three", "translation": "שלוש"},
    {"id": 132, "word": "state", "translation": "מדינה / מצב"},
    {"id": 133, "word": "never", "translation": "מעולם לא"},
    {"id": 134, "word": "become", "translation": "להפוך ל..."},
    {"id": 135, "word": "between", "translation": "בין"},
    {"id": 136, "word": "high", "translation": "גבוה"},
    {"id": 137, "word": "really", "translation": "באמת"},
    {"id": 138, "word": "something", "translation": "משהו"},
    {"id": 139, "word": "another", "translation": "אחר / נוסף"},
    {"id": 140, "word": "much", "translation": "הרבה (לא ספיר)"},
    {"id": 141, "word": "family", "translation": "משפחה"},
    {"id": 142, "word": "own", "translation": "של עצמו / להחזיק"},
    {"id": 143, "word": "leave", "translation": "לעזוב"},
    {"id": 144, "word": "put", "translation": "להניח / לשים"},
    {"id": 145, "word": "old", "translation": "ישן / זקן"},
    {"id": 146, "word": "while", "translation": "בזמן ש..."},
    {"id": 147, "word": "mean", "translation": "להתכוון"},
    {"id": 148, "word": "keep", "translation": "לשמור"},
    {"id": 149, "word": "student", "translation": "תלמיד / סטודנט"},
    {"id": 150, "word": "why", "translation": "למה"},
    {"id": 151, "word": "let", "translation": "לאפשר / לתת"},
    {"id": 152, "word": "great", "translation": "נהדר / גדול"},
    {"id": 153, "word": "same", "translation": "אותו הדבר"},
    {"id": 154, "word": "big", "translation": "גדול"},
    {"id": 155, "word": "group", "translation": "קבוצה"},
    {"id": 156, "word": "begin", "translation": "להתחיל"},
    {"id": 157, "word": "seem", "translation": "להיראות (נדמה)"},
    {"id": 158, "word": "country", "translation": "מדינה"},
    {"id": 159, "word": "help", "translation": "לעזור / עזרה"},
    {"id": 160, "word": "talk", "translation": "לדבר"},
    {"id": 161, "word": "where", "translation": "איפה"},
    {"id": 162, "word": "turn", "translation": "לפנות / תור"},
    {"id": 163, "word": "problem", "translation": "בעיה"},
    {"id": 164, "word": "every", "translation": "כל"},
    {"id": 165, "word": "start", "translation": "להתחיל"},
    {"id": 166, "word": "hand", "translation": "יד"},
    {"id": 167, "word": "might", "translation": "עשוי / עוצמה"},
    {"id": 168, "word": "American", "translation": "אמריקאי"},
    {"id": 169, "word": "show", "translation": "להראות / תוכנית"},
    {"id": 170, "word": "part", "translation": "חלק"},
    {"id": 171, "word": "against", "translation": "נגד"},
    {"id": 172, "word": "place", "translation": "מקום"},
    {"id": 173, "word": "such", "translation": "כזה"},
    {"id": 174, "word": "again", "translation": "שוב"},
    {"id": 175, "word": "few", "translation": "מעט"},
    {"id": 176, "word": "case", "translation": "מקרה / תיק"},
    {"id": 177, "word": "week", "translation": "שבוע"},
    {"id": 178, "word": "company", "translation": "חברה (עסקית)"},
    {"id": 179, "word": "system", "translation": "מערכת"},
    {"id": 180, "word": "each", "translation": "כל אחד"},
    {"id": 181, "word": "right", "translation": "נכון / ימין"},
    {"id": 182, "word": "program", "translation": "תוכנית"},
    {"id": 183, "word": "hear", "translation": "לשמוע"},
    {"id": 184, "word": "so", "translation": "אז"},
    {"id": 185, "word": "question", "translation": "שאלה"},
    {"id": 186, "word": "during", "translation": "במהלך"},
    {"id": 187, "word": "work", "translation": "עבודה"},
    {"id": 188, "word": "play", "translation": "לשחק"},
    {"id": 189, "word": "government", "translation": "ממשלה"},
    {"id": 190, "word": "run", "translation": "לרוץ / לנהל"},
    {"id": 191, "word": "small", "translation": "קטן"},
    {"id": 192, "word": "number", "translation": "מספר"},
    {"id": 193, "word": "off", "translation": "כבוי / מחוץ ל..."},
    {"id": 194, "word": "always", "translation": "תמיד"},
    {"id": 195, "word": "move", "translation": "לזוז / להזיז"},
    {"id": 196, "word": "night", "translation": "לילה"},
    {"id": 197, "word": "live", "translation": "לחיות / לגור"},
    {"id": 198, "word": "Mr", "translation": "מר (אדון)"},
    {"id": 199, "word": "point", "translation": "נקודה"},
    {"id": 200, "word": "believe", "translation": "להאמין"}
]

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("שינון מילים")
        BG_COLOR = "#111827"
        self.root.configure(bg=BG_COLOR)

        self.counter = 0
        self.pending_queue = []
        self.ignored_ids = []
        self.current_word = None

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        main_frame = tk.Frame(root, bg=BG_COLOR)
        main_frame.grid(row=0, column=0)

        self.word_label = tk.Label(main_frame, text="", font=("Helvetica", 36, "bold"), bg=BG_COLOR, fg="#F9FAFB")
        self.word_label.pack(pady=(0, 5))

        self.trans_label = tk.Label(main_frame, text="", font=("Helvetica", 20), bg=BG_COLOR, fg="#9CA3AF")
        self.trans_label.pack(pady=(0, 15))

        self.show_btn = tk.Button(
            main_frame, text=rev("הצג תרגום"), font=("Helvetica", 13), 
            command=self.show_translation, bg="#374151", fg="#F9FAFB", 
            bd=0, highlightthickness=0, relief="flat", activebackground="#4B5563",
            padx=15, pady=8
        )
        self.show_btn.pack(pady=(0, 25))

        self.know_btn = tk.Button(
            main_frame, text=rev("מכיר"), font=("Helvetica", 14, "bold"), 
            bg="#10B981", fg="white", width=18, height=1, command=self.handle_know, 
            bd=0, highlightthickness=0, relief="flat", activebackground="#059669"
        )
        self.know_btn.pack(pady=4)

        self.unknow_btn = tk.Button(
            main_frame, text=rev("לא מכיר"), font=("Helvetica", 14, "bold"), 
            bg="#F59E0B", fg="white", width=18, height=1, command=self.handle_unknow, 
            bd=0, highlightthickness=0, relief="flat", activebackground="#D97706"
        )
        self.unknow_btn.pack(pady=4)

        self.ignore_btn = tk.Button(
            main_frame, text=rev("אל תציג שוב"), font=("Helvetica", 13), 
            bg="#EF4444", fg="white", width=18, height=1, command=self.handle_ignore, 
            bd=0, highlightthickness=0, relief="flat", activebackground="#DC2626"
        )
        self.ignore_btn.pack(pady=4)

        self.update_card()

    def get_next_word(self):
        self.counter += 1

        for idx, item in enumerate(self.pending_queue):
            if item["trigger_at"] <= self.counter:
                word_id = item["id"]
                self.pending_queue.pop(idx)
                return next((w for w in WORDS if w["id"] == word_id), None)

        pending_ids = [item["id"] for item in self.pending_queue]
        available = [
            w for w in WORDS 
            if w["id"] not in self.ignored_ids and w["id"] not in pending_ids
        ]

        if not available:
            return None

        return random.choice(available)

    def update_card(self):
        self.current_word = self.get_next_word()
        self.trans_label.config(text="")
        
        if self.current_word:
            self.word_label.config(text=self.current_word["word"])
        else:
            self.word_label.config(text=rev("סיימת את כל המילים!"))
            self.show_btn.pack_forget()

    def show_translation(self):
        if self.current_word:
            self.trans_label.config(text=rev(self.current_word["translation"]))

    def handle_know(self):
        if self.current_word:
            self.update_card()

    def handle_unknow(self):
        if self.current_word:
            self.pending_queue.append({
                "id": self.current_word["id"],
                "trigger_at": self.counter + 10
            })
            self.update_card()

    def handle_ignore(self):
        if self.current_word:
            self.ignored_ids.append(self.current_word["id"])
            self.update_card()

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()
