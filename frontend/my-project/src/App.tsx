import SoldiersList from './components/Soldiers/SoldiersList.tsx';
import { soldiersMock } from './mocks/soldierssMock.ts'

function App() {
  return (
   <>
      <h1>DutyRoster - Soldiers</h1>
      <SoldiersList />
    </>
  );
}

export default App;
