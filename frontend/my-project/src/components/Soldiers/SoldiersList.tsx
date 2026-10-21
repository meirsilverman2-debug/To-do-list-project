import { useState } from 'react'
import { soldiersMock } from '../../mocks/soldierssMock';
import SoldiersCard from './SoldiersCard';


export default function SoldiersList() {
    const [search, setSearch] = useState("");

    const filterdSoldier = soldiersMock.filter((soldier) => {
        const searchValue = search.toLowerCase();
        
    return (
        soldier.name.toLowerCase().includes(searchValue) ||
        soldier.personal_number.includes(searchValue)
    );
    });



  return (
    <section>
        <h1>ניהול חיילים</h1>
        
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
