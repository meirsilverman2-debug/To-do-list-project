import { useState } from 'react';
import { soldiersMock } from '../../mocks/soldierssMock.ts';
import SoldiersCard from './SoldiersCard.tsx';
import type {Soldier} from "../../types.ts";
import SoldiersForm from './SoldiersForm.tsx';

export default function SoldiersList() {
    const [search, setSearch] = useState("");
    const [soldiers, setSoldiers] = useState<Soldier[]>(soldiersMock);

    function handleAddSoldier(name: string, personalNumber: string){

        const exists = soldiers.some(
            (soldier) => soldier.personal_number === personalNumber
        );
        
        if (exists) {
            alert("חייל עם מספר אישי זה כבר קיים");
            return;
        }


        const newSoldier: Soldier = {
            name: name,
            personal_number: personalNumber,
            role: "SOLDIER",
            commander_id: "blabla"
        };

        setSoldiers((currenrSoldier) => [
            ...currenrSoldier,
            newSoldier,
        ]);
    }

    const filterdSoldier = soldiers.filter((soldier) => {
        const searchValue = search.toLowerCase();
        
    return (
        soldier.name.toLowerCase().includes(searchValue) ||
        soldier.personal_number.includes(searchValue)
    );
    });



  return (
    <section>
        <h1>ניהול חיילים</h1>
        <SoldiersForm onAddSoldier={handleAddSoldier}/>

        <input
        type="text"
        placeholder='חיפוש לפי שם או מספר  אישי'
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        />

        <div>
            {filterdSoldier.map((soldier) => (
            <SoldiersCard
            key={soldier.personal_number}
            soldier={soldier}
            />
            ))}
        </div>

        {filterdSoldier.length === 0 && (
            <p>לא נמצאו חיילים</p>
        )}
    </section>
  );
}
