import { Component, OnInit } from '@angular/core';
import { AllservicesService } from '../services/allservices.service';
import { Profile, User } from '../interfaces/api';

@Component({
  selector: 'app-profile',
  standalone: true,
  imports: [],
  templateUrl: './profile.component.html',
  styleUrl: './profile.component.css'
})
export class ProfileComponent implements OnInit {
  user_id: number = 0;
  profile: User = 
  {
    id: 0,
    username: "",
    email: "",
    first_name: "",
    last_name: ""
}

profileData: Profile = {
  first_name: '',
  last_name: '',
  gender: '',
  date_of_birth_day: 0,
  date_of_birth_month: 0,
  date_of_birth_year: 1,
};

  constructor(private profileService: AllservicesService) {}

  ngOnInit(): void {
    this.loadProfile();
  }

  loadProfileData(){
    this.user_id = this.profile.id
    this.profileService.getPofileData(this.user_id).subscribe((data) => {
      this.profileData = data;
    });
  }
  loadProfile(): void {
    this.profileService.getProfile().subscribe(
      data => {
        this.profile = data;
      },
      error => {
        console.error('Error fetching profile', error);
      }
    );
    this.loadProfileData();
  }
}
