import { Component, OnInit } from '@angular/core';
import { Position } from '../../interfaces/api';
import { AllservicesService } from '../../services/allservices.service';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, RouterLink } from '@angular/router';

@Component({
  selector: 'app-casting-details',
  standalone: true,
  imports: [CommonModule, RouterLink],
  templateUrl: './casting-details.component.html',
  styleUrl: './casting-details.component.css'
})
export class CastingDetailsComponent implements OnInit{
  positions: Position[] = [];
  id: number = 1

  constructor(private myService: AllservicesService,  private route: ActivatedRoute){}

  ngOnInit(): void {
    this.id = this.route.snapshot.params['id'];
    this.getPositions();
  }

  getPositions(){
    this.myService.getPositionsByCasting(this.id).subscribe((positions) => {
      this.positions = positions;
    })
  }


}
