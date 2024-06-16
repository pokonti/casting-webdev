import { Component, OnInit } from '@angular/core';
import { Position } from '../../interfaces/api';
import { AllservicesService } from '../../services/allservices.service';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, RouterLink } from '@angular/router';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-casting-details',
  standalone: true,
  imports: [CommonModule, RouterLink, FormsModule],
  templateUrl: './casting-details.component.html',
  styleUrl: './casting-details.component.css'
})
export class CastingDetailsComponent implements OnInit{
  positions: Position[] = [];
  id: number = 1;
  logged: Boolean = false;
  username: string = "";
  password: string = "";

  constructor(private myService: AllservicesService,  private route: ActivatedRoute){}

  ngOnInit(): void {
    this.id = this.route.snapshot.params['id'];
    const access = localStorage.getItem("access");
    if(access) {
      this.logged = true;
      this.getPositions();
    }
   
  }

  getPositions(){
    this.myService.getPositionsByCasting(this.id).subscribe((positions) => {
      // console.log(positions);
      this.positions = positions;
    })
  }

  login(){
    this.myService.login(this.username, this.password).subscribe((data) => {
      this.logged = true;
      localStorage.setItem("access", data.access);
      localStorage.setItem("refresh", data.refresh);
      this.getPositions();
      window.location.reload();
    })
    
  }


}
