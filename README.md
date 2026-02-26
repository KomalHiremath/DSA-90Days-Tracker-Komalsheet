Quick notes

🔁 LIST →
List → Tuple → tuple(lst)
List → Set → set(lst)
List → String → "".join(lst)
List → String (with separator) → " ".join(lst)
List → Dictionary (pairs) → dict(lst)
List → Dictionary (index mapping) → {i: v for i, v in enumerate(lst)}

🔁 TUPLE →
Tuple → List → list(t)
Tuple → Set → set(t)
Tuple → String → "".join(t)
Tuple → Dictionary (pairs) → dict(t)

🔁 SET →
Set → List → list(s)
Set → Tuple → tuple(s)
Set → String → "".join(s)
Set → Dictionary → {x: None for x in s}


🔁 STRING →
String → List → list(s)
String → List (split) → s.split()
String → Tuple → tuple(s)
String → Set → set(s)
String → Dictionary (frequency) → dict(Counter(s))


🔁 DICTIONARY →
Dict → List (keys) → list(d.keys())
Dict → List (values) → list(d.values())
Dict → List (items) → list(d.items())
Dict → Tuple → tuple(d.items())
Dict → Set → set(d.keys())
Dict → String → str(d)




                   

