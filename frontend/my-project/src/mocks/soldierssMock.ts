import type { Soldier } from "../types";

export const soldiersMock: Soldier[] = [
  {
    personal_number: "1234567",
    name: "David Cohen",
    role: "COMMANDER",
    commander_id: null,
    
  },
  {
    personal_number: "2345678",
    name: "Daniel Levi",
    role: "SOLDIER",
    commander_id: "blabla",
    
  },
  {
    personal_number: "3456789",
    name: "Noam Israel",
    role: "SOLDIER",
    commander_id: null,
  },
  {
    personal_number: "4567890",
    name: "Amit Cohen",
    role: "SOLDIER",
    commander_id: "blabla",
  },
];