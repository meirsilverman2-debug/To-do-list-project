import { useState } from "react";

interface SoldierFormProps {
  onAddSoldier: (name: string, personalNumber: string) => void;
}

export default function SoldiersForm({ onAddSoldier }: SoldierFormProps) {
  const [name, setName] = useState("");
  const [personalNumber, setPersonalNumber] = useState("");

  function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();

    if (!name.trim() || !personalNumber.trim()) {
        return;
    }


    onAddSoldier(name.trim(), personalNumber.trim());

    setName("");
    setPersonalNumber("");
  }

  return(
  <form onSubmit={handleSubmit}>
    <h2>הוספת חייל</h2>

     <label htmlFor="soldier-name">שם החייל</label>
      <input
        id="soldier-name"
        type="text"
        value={name}
        onChange={(event) => setName(event.target.value)}
        placeholder="הכנס שם מלא"
        required
      />

      <label htmlFor="personal-number">מספר אישי</label>
      <input
        id="personal-number"
        type="text"
        value={personalNumber}
        onChange={(event) => setPersonalNumber(event.target.value)}
        placeholder="הכנס מספר אישי"
        required
      />

      <button type="submit">הוסף חייל</button>
    </form>
);}
