// 1. טיפוסים קבועים (Enums)
export type UserRole = 'COMMANDER' | 'SOLDIER';

export type TaskStatus = 'PENDING' | 'IN_PROGRESS' | 'COMPLETED';

export type DayOfWeek =
  | 'ראשון'
  | 'שני'
  | 'שלישי'
  | 'רביעי'
  | 'חמישי'
  | 'שישי'
  | 'שבת';

// 2. ישות חייל / מפקד (Soldier)
export interface Soldier {
  personal_number: string;
  name: string;
  role: UserRole;
  commander_id?: string | null;
  // לא שולחים סיסמה לפרונטאנד מטעמי אבטחה
}

// 3. ישות משימה (Task)
export interface Task {
  id: number;
  title: string;
  description: string;
  status: TaskStatus;
  day: DayOfWeek | string;
  soldier_id: number;
  // נתוני החייל שמגיעים ב-JOIN מ-Supabase:
  soldiers?: {
    name: string;
    personal_number: string;
    role: UserRole;
  };
}

// 4. טיפוס ליצירת משימה חדשה (מה שהמפקד שולח בטופס)
export interface CreateTaskPayload {
  title: string;
  description: string;
  day: DayOfWeek | string;
  soldier_id: number;
  status?: TaskStatus;
}

export interface login {
    personal_number: string;
    password: string;

}

export interface CreateSoldierPayload {
    personal_number: string;
    name: string;
    password: string;
    commander_id?: string | null;
}