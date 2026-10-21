import type {Soldier} from "../../types";


interface SoldiersCardProps {
    soldier: Soldier;
}

export default function SoldiersCard({soldier}: SoldiersCardProps) {
  return (
    <div>
        <h3>{soldier.name}</h3>

        <p>מספר אישי: {soldier.personal_number}</p>

        <p>
            תפקיד:{" "}
            {soldier.role === "COMMANDER" ? "חייל" : "מפקד"}
        </p>
    </div>
  )
}
