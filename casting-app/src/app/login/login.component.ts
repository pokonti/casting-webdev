import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent implements OnInit{
  
  logged: Boolean = false;
  username: string = "";
  password: string = "";

  ngOnInit(): void {
    const access = localStorage.getItem("access");
  }

}
