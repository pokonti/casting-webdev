import { Component, OnInit } from '@angular/core';
import { FooterComponent } from "../footer/footer.component";
import { FormsModule } from '@angular/forms';


class Profile{
    constructor(public first_name: string,
        public last_name: string,
        public gender: string)
    { }
}

@Component({
    selector: 'app-form',
    standalone: true,
    templateUrl: './form.component.html',
    styleUrl: './form.component.css',
    imports: [FooterComponent, FormsModule]
})
export class FormComponent implements OnInit{
 
    first_name: string = '';
    last_name: string = '';
    gender: string = '';
    genders: string[] = ["Male", "Female"];
    dd!: number;
    mm!: number;
    yyyy!: number;
    users: Profile[] = [];

    ngOnInit(): void {
        console.log(this.users)
    }

    addProfile(){
        this.users.push(new Profile(this.first_name, this.last_name, this.gender));
    }


    
}
