import { Component, Input } from '@angular/core';
import { FooterComponent } from "../footer/footer.component";
import { FormsModule } from '@angular/forms';
import { AllservicesService } from '../../services/allservices.service';
import { Position, Profile, ProfileAndPosition } from '../../interfaces/api';
import { ActivatedRoute } from '@angular/router';
import { response } from 'express';
import { error } from 'console';

@Component({
    selector: 'app-form',
    standalone: true,
    templateUrl: './form.component.html',
    styleUrl: './form.component.css',
    imports: [FooterComponent, FormsModule]
})
export class FormComponent{
    positionId: number = 0;

    position: Position = {
        id: 0,
        name: '',
        requirements: '',
        casting: {
            id: 0,
            name: '',
            description: '',
            photo: ''
        }
    };

    profile: Profile = {
        first_name: '',
        last_name: '',
        gender: '',
        date_of_birth_day: 0,
        date_of_birth_month: 0,
        date_of_birth_year: 0,
    };

    constructor(private service: AllservicesService, private route: ActivatedRoute) { }

    ngOnInit(): void {
        this.route.queryParams.subscribe(params => {
          this.positionId = +params['positionId'];
        });
        this.getPositionInfo();
    }

    getPositionInfo(){
        this.service.getPositionById(this.positionId).subscribe(position => {
            this.position = position;
        });
    }
      
    onSubmit(): void {
        const data: ProfileAndPosition = {
            applicant: this.profile,
            position: this.position
        };
        
        // console.log('Submitting data:', data);

        // this.service.createCasting(this.profile).subscribe(
        //     response => console.log('Form created successfully:', response),
        //     error => console.error('Error sending form:', error)
        // );
        this.service.connectPositionWithApplicant(data).subscribe(
            response => console.log('Data is sent successfully:', response),
            error => console.error('Error:', error)
        );
        // empty fields again
        this.profile = {
            first_name: '',
            last_name: '',
            gender: '',
            date_of_birth_day: 0,
            date_of_birth_month: 0,
            date_of_birth_year: 0,
        };
      }





    


    
}
