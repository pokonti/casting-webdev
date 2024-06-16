import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import {Router, RouterLink, RouterLinkActive, RouterOutlet} from "@angular/router";

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [
    RouterLink,
    RouterLinkActive,
    RouterOutlet,
    CommonModule
  ],
  templateUrl: './header.component.html',
  styleUrl: './header.component.css'
})
export class HeaderComponent implements OnInit{
  logged: Boolean = false;
  message: string = "You logged out!"
  private isLocalStorageAvailable = typeof localStorage !== 'undefined';

  constructor(private router: Router) {}
  ngOnInit(): void {
    if (this.isLocalStorageAvailable){
      const access = localStorage.getItem("access");
      if(access) {
        this.logged = true;
      }
    }
 
  }
  
  logout(){
    localStorage.removeItem("access");
    localStorage.removeItem("refresh");
    this.router.navigate(['/home']).then(() => {
      window.location.reload();
    });
    alert(this.message);
  }
  
}

