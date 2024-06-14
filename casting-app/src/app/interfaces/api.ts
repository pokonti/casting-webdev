export interface Casting{
    id: number;
    name: string;
    description: string;
    photo: string;
}

export interface Position{
    id: number;
    name: string;
    requirements: string;
    casting: Casting;
}

export interface Ad{
    title: string;
    description: string;
    photo: string;
}

export interface Profile {
    first_name: string;
    last_name: string;
    gender: string;
    date_of_birth_day: number;
    date_of_birth_month: number;
    date_of_birth_year: number;
}

export interface Casting {
    id: number;
    name: string;
    description: string;
    photo: string;
}
  
export interface Position {
    id: number;
    casting: Casting;
    name: string;
    requirements: string;
}
export interface ProfileAndPosition {
    applicant: Profile;
    position: Position;
}