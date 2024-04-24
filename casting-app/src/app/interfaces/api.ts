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